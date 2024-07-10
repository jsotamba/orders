import django_filters
from django.utils import timezone

from apps.order.models import Order


class OrderFilter(django_filters.FilterSet):
    current_date = django_filters.BooleanFilter(method='filter_current_date')
    min_date = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    max_date = django_filters.DateFilter(field_name="date", lookup_expr='lte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['min_date', 'max_date', 'name', 'description', 'current_date']

    def filter_current_date(self, queryset, name, value):
        if value:
            today = timezone.now().date()
            queryset = queryset.filter(date=today)
        return queryset
