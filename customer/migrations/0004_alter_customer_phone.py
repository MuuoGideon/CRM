# Generated by Django 5.1.3 on 2024-11-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_remove_customer_address_customer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
