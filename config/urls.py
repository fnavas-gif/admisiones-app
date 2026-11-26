from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aspirantes/', include('admisiones.urls.aspirante_urls')),
    path('carreras/', include('admisiones.urls.carrera_urls')),
    path('solicitudes/', include('admisiones.urls.solicitud_urls')),
    path('documentos/', include('admisiones.urls.documento_urls')),
    path('cuentas/', include('admisiones.urls.auth_urls')),
]