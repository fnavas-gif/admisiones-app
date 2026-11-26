from django.urls import path, include

urlpatterns = [
    path('', include('admisiones.urls.aspirante_urls')),
    path('carreras/', include('admisiones.urls.carrera_urls')),
    path('solicitudes/', include('admisiones.urls.solicitud_urls')),
    path('documentos/', include('admisiones.urls.documento_urls')),
]