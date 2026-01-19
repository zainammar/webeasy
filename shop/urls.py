from django.urls import path
from . import views

urlpatterns = [
    # Cart pages must come **before** the slug path
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/decrease/<int:product_id>/', views.cart_decrease, name='cart_decrease'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    # Add product from product page
    path('<slug:slug>/add/', views.add_to_cart, name='add_to_cart'),

    # Product list and product detail
    path('', views.product_list, name='product_list'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),  # generic slug route last
]
