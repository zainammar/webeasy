from django.urls import path
from .views import page_detail
from .models import Page

# get default page slug, e.g., 'home'
default_page = Page.objects.filter(slug='home').first()
default_slug = default_page.slug if default_page else None

urlpatterns = [
    # Home page at '/'
    path('', page_detail, {'slug': default_slug}, name='home'),

    # All other pages by slug
    path('<slug:slug>/', page_detail, name='page_detail'),
]
