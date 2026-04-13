from django.shortcuts import render, get_object_or_404
from .models import Page

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)  # is_published=True hata diya
    all_pages = Page.objects.all()  # ye theek hai
    return render(request, 'themeOne/home.html', {
        'page': page,
        'all_pages': all_pages,
    })