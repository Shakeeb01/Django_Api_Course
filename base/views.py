from .models import (
    Product,Order,
    OrderItem,User
)
from .serializers import (
    ProductSerializer,
    OrderSerializer,
    OrderItemSerializer
)
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# _________________________________________________________________________________________________________________ #

# All Products
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    
# Single Product
@api_view(['GET'])
def product_detail(request,pk):
    product = get_object_or_404(Product,pk = pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


# All Orders
@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
    