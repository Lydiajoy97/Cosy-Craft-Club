# Generated by Django 4.2.9 on 2024-02-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_uploads_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploads',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
