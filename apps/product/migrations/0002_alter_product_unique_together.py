# Generated by Django 5.0.7 on 2024-07-10 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="product",
            unique_together={("name", "price")},
        ),
    ]
