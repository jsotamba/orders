from django.urls import path
from apps.order.api.api import order_api_view, filter_api_view, order_detail_api_view

urlpatterns = [
    path('', order_api_view, name='order_api_view'),
    path('filter/', filter_api_view, name='filter_api_view'),
    path('<int:pk>/', order_detail_api_view, name='order_detail_api_view'),
]