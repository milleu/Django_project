# Generated by Django 4.2.5 on 2024-02-26 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_manufactured_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='manufactured_at',
        ),
    ]