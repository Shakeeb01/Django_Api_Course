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