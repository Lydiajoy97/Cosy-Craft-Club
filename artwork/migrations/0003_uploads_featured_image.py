# Generated by Django 4.2.9 on 2024-02-18 22:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0002_rating_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploads',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
