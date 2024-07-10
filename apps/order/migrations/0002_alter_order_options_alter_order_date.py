# Generated by Django 5.0.7 on 2024-07-10 09:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "ordering": ["date"],
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
