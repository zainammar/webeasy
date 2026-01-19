from django.urls import path
from .views import page_detail
from .models import Page

# default slug for home
default_page = Page.objects.filter(slug='home').first()
default_slug = default_page.slug if default_page else None

urlpatterns = [
    path('', page_detail, {'slug': default_slug}, name='home'),
    path('<slug:slug>/', page_detail, name='page_detail'),
]
