from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product

class ProductView(ListView):
    model = Product
    template_name = 'product/products.html'
    context_object_name = 'product_list'


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product-details.html'