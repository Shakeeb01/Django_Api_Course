from .models import Product,Order,OrderItem,User
from .serializers import ProductSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

# ___________________________________________________________________________ #

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def product_detail(request,pk):
    product = get_object_or_404(Product,pk = pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)