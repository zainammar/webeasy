from django.urls import path
from . import views

urlpatterns = [
    # Cart URLs FIRST - these are specific paths
    path('cart/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),

    # Then product detail - this is a specific item
    path('<slug:slug>/', views.product_detail, name='product_detail'), # <--- MOVED THIS UP

    # Then category filter - this is a general filter
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'), # <--- ADDED 'category/' PREFIX

    # Finally, the base product list (all products)
    path('', views.product_list, name='product_list'),
]