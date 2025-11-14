from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product

class ProductView(ListView):
    model = Product
    template_name = 'product/products.html'
    context_object_name = 'product_list'
    ordering = ['-created_at']


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product-details.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'
    login_url = 'login'


class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'user/settings.html'
    login_url = 'login'



class UserLoginView(TemplateView):
    template_name = 'auth/login.html'


class UserRegisterView(TemplateView):
    template_name = 'auth/register.html'