# Generated by Django 5.0.3 on 2024-06-27 16:22

import image_cropping.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_alter_mainpage_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='header_image',
            field=image_cropping.fields.ImageCropField(upload_to='header_images/'),
        ),
    ]
