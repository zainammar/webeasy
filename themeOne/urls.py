from django.urls import path
from . import views

urlpatterns = [
    # Home page (static slug)
    path('', views.page_detail, {'slug': 'home'}, name='home'),

    # Dynamic pages
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]