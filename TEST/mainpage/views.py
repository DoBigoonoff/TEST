from django.shortcuts import render
from .models import MainPage

def main_page(request):
    page = MainPage.objects.first()
    return render(request, 'mainpage/main_page.html', {'page': page})
