from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.product.models import Product
from apps.product.api.serializers import ProductSerializer

from drf_yasg.utils import swagger_auto_schema

from utils.messages import get_message_by_code, MessageEnum


@swagger_auto_schema(methods=['post'], request_body=ProductSerializer)
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
            return Response(get_message_by_code(MessageEnum.CREATED), status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, pk):
    product = Product.objects.filter(pk=pk).first()

    # validation
    if product:

        # retrieve
        if request.method == 'GET':
            product_serializer = ProductSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            product_serializer = ProductSerializer(product, data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(get_message_by_code(MessageEnum.UPDATED), status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            product.delete()
            return Response(get_message_by_code(MessageEnum.DELETED), status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(get_message_by_code(MessageEnum.NOT_FOUND), status=status.HTTP_404_NOT_FOUND)
