# Generated by Django 5.0.1 on 2024-03-07 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_product_display_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]