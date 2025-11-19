from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    about = models.TextField()
    count = models.IntegerField(default=0)
    sale = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    info = models.JSONField(default=dict)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def sale_price(self):
        return self.price - (self.price * self.sale / 100)
    
    @property
    def is_stok(self):
        if self.count > 0:
            return True
        return False
    

    @property
    def is_new(self):
        return now() - timedelta(days=3) < self.created_at

    def __str__(self):
        return self.name
    
    # class Meta:
    #     ordering = ['-created_at']



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name


class Users(AbstractUser):
    phone = models.CharField(max_length=25, unique=True, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    banner = models.ImageField(upload_to='banner/', blank=True, null=True)

    def __str__(self):
        return self.username


