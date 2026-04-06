# shop/models.py

from django.db import models
from django.contrib.auth.models import User # For linking to the User model in Order
from django.utils.text import slugify # For automatically generating slugs
from django.db.models import Index # For defining database indexes

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',) # Order categories alphabetically by name
        verbose_name = 'category'
        verbose_name_plural = 'categories' # Correct plural for admin display

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Automatically generate slug from name if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # You can add a method here to get the URL for a specific category page
    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products', # Allows you to access products from a category instance (e.g., category.products.all())
        on_delete=models.CASCADE, # If a category is deleted, all its products are also deleted
        null=True,   # Allows products to initially exist without a category (useful for migration)
        blank=True   # Allows the category field to be blank in forms
    )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True) # Organizes uploads by date
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) # Automatically sets creation timestamp
    updated = models.DateTimeField(auto_now=True) # Automatically updates timestamp on every save

    class Meta:
        ordering = ('name',) # Order products alphabetically by name
        # Define database indexes for improved query performance
        indexes = [
            Index(fields=['id', 'slug']), # Composite index for ID and slug
            Index(fields=['name']),      # Index on the product name
            Index(fields=['-created']),  # Index for ordering by creation date (e.g., for "new arrivals")
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Automatically generate slug from name if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # You can add a method here to get the URL for a specific product detail page
    # def get_absolute_url(self):
    #     from django.urls import reverse
    #     return reverse('shop:product_detail', args=[self.id, self.slug])

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Links an order to a user
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    completed = models.BooleanField(default=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) # Links an item to a specific order
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # Links an item to a specific product
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # Price at the time of purchase

    def item_total(self):
        return self.price * self.quantity # Calculates the total price for this item in the order