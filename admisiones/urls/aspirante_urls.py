
from django.urls import path
from admisiones.views.aspirante_views import (
    listar_aspirantes,
    crear_aspirante,
    detalle_aspirante,
    editar_aspirante,
    eliminar_aspirante
)

urlpatterns = [
    path('', listar_aspirantes, name='listar_aspirantes'),
    path('crear/', crear_aspirante, name='crear_aspirante'),
    path('<int:pk>/', detalle_aspirante, name='detalle_aspirante'),
    path('<int:pk>/editar/', editar_aspirante, name='editar_aspirante'),
    path('<int:pk>/eliminar/', eliminar_aspirante, name='eliminar_aspirante'),
]
