from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [

    # ========================
    # 🔥 SPECIFIC ROUTES FIRST
    # ========================

    path('upload-payment-proof/', views.upload_payment_proof, name='upload_payment_proof'),

    path('cart/', views.cart_detail, name='cart_detail'),

    path('checkout/', views.checkout, name='checkout'),

    path('add-to-cart/<slug:slug>/', views.add_to_cart, name='add_to_cart'),

    path('success/', views.success_page, name='success_page'),
    # ========================
    # 📂 CATEGORY ROUTE
    # ========================
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),


    # ========================
    # 🧾 PRODUCT DETAIL (KEEP BEFORE EMPTY LIST)
    # ========================
    path('<slug:slug>/', views.product_detail, name='product_detail'),


    # ========================
    # 📦 PRODUCT LIST (HOME)
    # ========================
    path('', views.product_list, name='product_list'),
]