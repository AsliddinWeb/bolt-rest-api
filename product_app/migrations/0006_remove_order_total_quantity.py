# Generated by Django 4.2.7 on 2023-11-21 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_quantity',
        ),
    ]
