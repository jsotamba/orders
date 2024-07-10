from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.order.models import Order
from apps.order.api.serializers import OrderSerializer


@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        orders_serializer = OrderSerializer(orders, many=True)
        return Response(orders_serializer.data)

    elif request.method == 'POST':
        order_serializer = OrderSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
