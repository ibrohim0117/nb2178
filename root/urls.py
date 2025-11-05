from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from app.views import ProductView, ProductDetail

from root import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductView.as_view(), name='product_list'),
    path('product/', ProductDetail.as_view(), name='product'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
