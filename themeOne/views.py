from django.shortcuts import render
from .models import Page

def home(request):
    pages = Page.objects.all()
    return render(request, 'themeOne/home.html', {'pages': pages})
