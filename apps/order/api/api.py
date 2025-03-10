from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.order.models import Order
from apps.order.api.serializers import OrderSerializer, OrderCreateUpdateSerializer
from apps.order.utils.filters import OrderFilter
from utils.messages import MessageEnum, get_message_by_code

from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
def filter_api_view(request):
    queryset = Order.objects.all()
    filterset = OrderFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
        queryset = filterset.qs
    serializer = OrderSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(methods=['post'], request_body=OrderCreateUpdateSerializer)
@api_view(['GET', 'POST'])
def order_api_view(request):

    # list
    if request.method == 'GET':
        orders = Order.objects.all()
        orders_serializer = OrderSerializer(orders, many=True)
        return Response(orders_serializer.data, status=status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        order_serializer = OrderCreateUpdateSerializer(data=request.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(get_message_by_code(MessageEnum.CREATED), status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put'], request_body=OrderCreateUpdateSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
def order_detail_api_view(request, pk=None):
    order = Order.objects.filter(pk=pk).first()

    # validation
    if order:

        # retrieve
        if request.method == 'GET':
            order_serializer = OrderSerializer(order)
            return Response(order_serializer.data, status=status.HTTP_200_OK)

        # update
        elif request.method == 'PUT':
            order_serializer = OrderCreateUpdateSerializer(order, data=request.data)
            if order_serializer.is_valid():
                order_serializer.save()
                return Response(get_message_by_code(MessageEnum.UPDATED), status=status.HTTP_200_OK)
            return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # delete
        elif request.method == 'DELETE':
            order.delete()
            return Response(get_message_by_code(MessageEnum.DELETED), status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(get_message_by_code(MessageEnum.NOT_FOUND), status=status.HTTP_404_NOT_FOUND)