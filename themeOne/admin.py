from django.contrib import admin
from .models import Page
from .models import NavbarItem

admin.site.register(NavbarItem)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')  # ✅ remove created_at
    prepopulated_fields = {'slug': ('title',)}