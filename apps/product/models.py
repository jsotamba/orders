from django.db import models
from django.db.models import UniqueConstraint


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['name', 'price'], name='unique_name_price')
        ]
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        return self.name
