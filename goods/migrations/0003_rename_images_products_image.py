# Generated by Django 4.2 on 2024-01-12 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_products_discount_alter_products_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='images',
            new_name='image',
        ),
    ]
