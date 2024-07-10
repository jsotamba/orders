from django.contrib import admin

from apps.product.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
