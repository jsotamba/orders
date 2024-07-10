from django.contrib import admin

from apps.product.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name', 'price',)


admin.site.register(Product, ProductAdmin)
