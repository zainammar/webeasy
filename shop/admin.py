# shop/admin.py

from django.contrib import admin
from.models import Category, Product, Order, OrderItem # Import your new Category model!

from .models import PaymentProof

# Simple registration
admin.site.register(PaymentProof)

# Admin configuration for the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # Automatically fills the slug field as you type the name

# Admin configuration for the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'category', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category'] # Add 'category' to filters
    list_editable = ['price', 'available'] # Allows editing these fields directly from the list view
    prepopulated_fields = {'slug': ('name',)} # Automatically fills the slug field as you type the name

# Your existing OrderItemInline (no changes needed)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

# Your existing OrderAdmin (no changes needed)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_price', 'completed')
    inlines = [OrderItemInline]

# Note: You no longer need `admin.site.register(Product)` at the bottom
# because Product is now registered using the `@admin.register` decorator.