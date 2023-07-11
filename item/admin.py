from django.contrib import admin
from .models import Category, Item


class CategoryAdmin(admin.ModelAdmin):
    # Display specific columns to show in the panel
    list_display = ("name",)


admin.site.register(Category, CategoryAdmin)


class ItemAdmin(admin.ModelAdmin):
    # Display specific columns to show in the panel
    list_display = ("name", "description", "price", "image", "is_sold", "created_by", "created_at")


admin.site.register(Item, ItemAdmin)
