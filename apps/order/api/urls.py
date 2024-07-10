from django.urls import path
from apps.order.api.api import user_api_view

urlpatterns = [
    path('', user_api_view, name='api-user-view'),
]