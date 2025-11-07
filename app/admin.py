from django.contrib import admin
from .models import Product, Category, ProductImage

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name', ]


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 2


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name', 'count', 'is_active', 'price', 'sale', 'category', 'id']
    search_fields = ['name', 'count', 'price', 'is_active']
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImage(admin.ModelAdmin):
    list_display = ['product', 'image']
