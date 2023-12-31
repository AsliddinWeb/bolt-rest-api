# Generated by Django 4.2.7 on 2023-11-22 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0009_remove_product_count_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Kategoriyalar'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Buyurtmalar'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name_plural': 'Buyurtma berilgan maxsulotlar'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Maxsulotlar'},
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Buyurtma berildi'), ('2', 'Yetkazildi'), ('3', 'Bekor qilindi')], max_length=255),
        ),
    ]
