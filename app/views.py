from django.shortcuts import render
from django.views.generic import TemplateView

class ProductView(TemplateView):
    template_name = 'product/products.html'


class ProductDetail(TemplateView):
    template_name = 'product/product-details.html'