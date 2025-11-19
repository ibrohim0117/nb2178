from django.shortcuts import render, redirect
from django.views.generic import (
    TemplateView, ListView, DetailView,
    DeleteView, CreateView, FormView
)

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout

from .models import Product, Users
from .forms import UserRegisterForm, UserLoginForm

class ProductView(ListView):
    model = Product
    template_name = 'product/products.html'
    context_object_name = 'product_list'
    ordering = ['-created_at']


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/product-details.html'


# class ProfileView(LoginRequiredMixin, DetailView):
#     model = Users
#     context_object_name = 'people'
#     template_name = 'user/profile.html'
#     login_url = 'login'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['people'] = user
        return context

class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'user/settings.html'
    login_url = 'login'


    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)



class UserLoginView(FormView):
    form_class = UserLoginForm
    template_name = 'auth/login.html'
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = Users.objects.filter(username=username).first()
        if user and user.check_password(password):
            login(self.request, user)
            return redirect('/')
        return super().form_valid(form)


class UserRegisterView(CreateView):
    model = Users
    template_name = 'auth/register.html'
    form_class =  UserRegisterForm
    success_url = '/'


class UserLogoutView(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('/')