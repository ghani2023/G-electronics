from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Index/', views.Index.as_view(), name = 'Index'),
    path('products/', views.products.as_view(), name = 'products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
