from django.db import models
from image_cropping import ImageCropField, ImageRatioField

class MainPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    header_image = ImageCropField(upload_to='header_images/')
    cropping = ImageRatioField('header_image', '300x300')

    def __str__(self):
        return self.title
