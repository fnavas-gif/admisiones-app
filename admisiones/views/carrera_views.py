
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.deletion import ProtectedError
from django.contrib.auth.decorators import login_required, permission_required

from admisiones.models import Carrera
from admisiones.forms import CarreraForm


@login_required(login_url='login')
@permission_required('admisiones.view_carrera', raise_exception=True)
def listar_carreras(request):
    carreras = Carrera.objects.all()

    return render(
        request,
        'admisiones/carreras/listar.html',
        {'carreras': carreras}
    )


@login_required(login_url='login')
@permission_required('admisiones.add_carrera', raise_exception=True)
def crear_carrera(request):
    if request.method == 'POST':
        formulario = CarreraForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_carreras')
    else:
        formulario = CarreraForm()

    return render(
        request,
        'admisiones/carreras/formulario.html',
        {'formulario': formulario}
    )


@login_required(login_url='login')
@permission_required('admisiones.change_carrera', raise_exception=True)
def editar_carrera(request, pk):
    carrera = get_object_or_404(Carrera, pk=pk)

    if request.method == 'POST':
        formulario = CarreraForm(request.POST, instance=carrera)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_carreras')
    else:
        formulario = CarreraForm(instance=carrera)

    return render(
        request,
        'admisiones/carreras/formulario.html',
        {
            'formulario': formulario,
            'es_edicion': True,
            'carrera': carrera
        }
    )


@login_required(login_url='login')
@permission_required('admisiones.delete_carrera', raise_exception=True)
def eliminar_carrera(request, pk):
    carrera = get_object_or_404(Carrera, pk=pk)

    if request.method == 'POST':
        try:
            carrera.delete()
            return redirect('listar_carreras')

        except ProtectedError:
            return render(
                request,
                'admisiones/carreras/eliminar.html',
                {
                    'carrera': carrera,
                    'error': 'No se puede eliminar esta carrera porque tiene solicitudes asociadas.'
                }
            )

    return render(
        request,
        'admisiones/carreras/eliminar.html',
        {'carrera': carrera}
    )
