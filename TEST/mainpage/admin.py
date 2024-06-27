from django.contrib import admin
from .models import MainPage
from image_cropping.admin import ImageCroppingMixin

class MainPageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'content', 'cropping')

admin.site.register(MainPage, MainPageAdmin)
