from django.contrib import admin
from django.urls import path
from web.views import acerca, indice, bienvenido
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name='indice'),
    path('acerca/', acerca, name='acerca'),
    path('bienvenido/', bienvenido, name='bienvenido'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
