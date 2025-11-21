from django.contrib import admin
from .models import Product, Category, ProductImage, Users, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    search_fields = ['name', ]


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'is_active', 'price', 'sale_price', 'sale', 'category', 'id']
    search_fields = ['name', 'count', 'price', 'is_active']
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImage(admin.ModelAdmin):
    list_display = ['product', 'image']


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'phone', 'is_active', 'is_staff', 'id']
    search_fields = ['username', 'email', 'phone']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'created_at', 'id']
