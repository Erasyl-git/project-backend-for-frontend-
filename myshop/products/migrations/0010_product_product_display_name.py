# Generated by Django 5.0.1 on 2024-03-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_category_name_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_display_name',
            field=models.CharField(max_length=100, null=True, verbose_name='Отображаемое имя'),
        ),
    ]