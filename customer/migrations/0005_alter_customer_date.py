# Generated by Django 5.1.3 on 2024-11-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]