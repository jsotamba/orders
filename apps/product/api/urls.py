from django.urls import path
from apps.product.api.api import product_api_view

urlpatterns = [
    path('', product_api_view, name='product-api'),
]