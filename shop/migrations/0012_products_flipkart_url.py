# Generated by Django 5.0.7 on 2024-09-20 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_color_products_colors'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='flipkart_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
