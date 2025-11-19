from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from app.views import (
    ProductView, ProductDetail, ProfileView, 
    SettingsView, UserLoginView, UserRegisterView, UserLogoutView
)

from root import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product'),

    # users urls
    # path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('settings/', SettingsView.as_view(), name='settings'),

    # auth
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
