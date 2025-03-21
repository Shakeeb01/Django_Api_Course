from rest_framework import serializers
from .models import Product,User,Order,OrderItem


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            # 'description',
            'price',
            'stock'
        ]
        
    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater then 0.')
        return value
    
    
    
# Order Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source = 'product.name')
    product_price = serializers.DecimalField(source = 'product.price',max_digits=10,decimal_places=2)
    
    class Meta:
        model = OrderItem
        fields = [
            'product_name',
            'product_price',
            'quantity',
            'item_subtotal'
        ]



# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True,read_only=True)
    total_price = serializers.SerializerMethodField(method_name='_total')
    
    def _total(self,obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    
    class Meta:
        model = Order
        fields = [
            'order_id',
            'created_at',
            'user',
            'status',
            'items',
            'total_price',
        ]
        
        
# Product Info Serializer
# This serializer does not depend on any model of our db.
class ProductInfoSerializer(serializers.Serializer):
    # Getting all the products,count of products,max price
    # here we will specify fields that we want in our api data
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()