from django.db import models
from django.utils import timezone

from apps.product.models import Product


# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=timezone.now)
    products = models.ManyToManyField(Product, related_name='orders')

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['date']

    def __str__(self):
        return self.name
