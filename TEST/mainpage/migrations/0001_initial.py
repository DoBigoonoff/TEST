# Generated by Django 5.0.3 on 2024-06-27 15:33

import image_cropping.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('header_image', image_cropping.fields.ImageCropField(upload_to='header_images/')),
                ('cropping', image_cropping.fields.ImageRatioField('header_image', '800x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
            ],
        ),
    ]
