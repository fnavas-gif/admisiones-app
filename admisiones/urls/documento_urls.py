from django.urls import path
from admisiones.views.documento_views import (
    listar_documentos,
    crear_documento
)

urlpatterns = [
    path('', listar_documentos, name='listar_documentos'),
    path('crear/', crear_documento, name='crear_documento'),
]