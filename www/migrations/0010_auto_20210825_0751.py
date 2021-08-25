# Generated by Django 3.2.5 on 2021-08-25 07:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0009_alter_article_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]