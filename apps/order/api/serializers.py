from rest_framework import serializers
from apps.order.models import Order
from apps.product.api.serializers import ProductSerializer
from apps.product.models import Product


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'name', 'description', 'date', 'products']


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = ['name', 'description', 'date', 'products']
