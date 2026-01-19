from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),          # /shop/
    path('<slug:slug>/', views.product_detail, name='product_detail'),  # /shop/<product-slug>/
]
