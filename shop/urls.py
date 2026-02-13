from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    
    # Cart URLs FIRST
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),
    
    # Product detail LAST
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
