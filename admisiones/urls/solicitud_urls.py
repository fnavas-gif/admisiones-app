from django.urls import path
from admisiones.views.solicitud_views import (
    listar_solicitudes,
    crear_solicitud
)

urlpatterns = [
    path('', listar_solicitudes, name='listar_solicitudes'),
    path('crear/', crear_solicitud, name='crear_solicitud'),
]