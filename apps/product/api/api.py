from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.product.models import Product
from apps.product.api.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)
    if request.method == 'POST':
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)