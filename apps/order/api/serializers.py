from rest_framework import serializers
from apps.order.models import Order
from apps.product.api.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'name', 'description', 'date', 'products']
