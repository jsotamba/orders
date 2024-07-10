from django.contrib import admin

from apps.order.models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'date')
    search_fields = ('name', 'description')
    list_filter = ('date',)
    date_hierarchy = 'date'


admin.site.register(Order, OrderAdmin)