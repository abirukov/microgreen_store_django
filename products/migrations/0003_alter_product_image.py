# Generated by Django 5.0b1 on 2023-11-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(null=True, upload_to="uploads/product/images"),
        ),
    ]
