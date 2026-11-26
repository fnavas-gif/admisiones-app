
from django.urls import path
from admisiones.views.carrera_views import (
    listar_carreras,
    crear_carrera,
    editar_carrera,
    eliminar_carrera
)

urlpatterns = [
    path('', listar_carreras, name='listar_carreras'),
    path('crear/', crear_carrera, name='crear_carrera'),
    path('<int:pk>/editar/', editar_carrera, name='editar_carrera'),
    path('<int:pk>/eliminar/', eliminar_carrera, name='eliminar_carrera'),
]
