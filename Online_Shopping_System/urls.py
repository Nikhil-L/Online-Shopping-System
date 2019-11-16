
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('customer/', include('customer.urls')),
    path('orders/', include('orders.urls')),
    path('', views.homepage, name = 'home')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
