
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from admisiones.models import Aspirante
from admisiones.forms import AspiranteForm


@login_required(login_url='login')
@permission_required('admisiones.view_aspirante', raise_exception=True)
def listar_aspirantes(request):
    aspirantes = Aspirante.objects.all()

    return render(
        request,
        'admisiones/aspirantes/listar.html',
        {'aspirantes': aspirantes}
    )


@login_required(login_url='login')
@permission_required('admisiones.add_aspirante', raise_exception=True)
def crear_aspirante(request):
    if request.method == 'POST':
        formulario = AspiranteForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_aspirantes')
    else:
        formulario = AspiranteForm()

    return render(
        request,
        'admisiones/aspirantes/formulario.html',
        {'formulario': formulario}
    )


@login_required(login_url='login')
@permission_required('admisiones.view_aspirante', raise_exception=True)
def detalle_aspirante(request, pk):
    aspirante = get_object_or_404(Aspirante, pk=pk)

    return render(
        request,
        'admisiones/aspirantes/detalle.html',
        {'aspirante': aspirante}
    )


@login_required(login_url='login')
@permission_required('admisiones.change_aspirante', raise_exception=True)
def editar_aspirante(request, pk):
    aspirante = get_object_or_404(Aspirante, pk=pk)

    if request.method == 'POST':
        formulario = AspiranteForm(request.POST, instance=aspirante)

        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_aspirante', pk=aspirante.pk)
    else:
        formulario = AspiranteForm(instance=aspirante)

    return render(
        request,
        'admisiones/aspirantes/formulario.html',
        {
            'formulario': formulario,
            'es_edicion': True,
            'aspirante': aspirante
        }
    )


@login_required(login_url='login')
@permission_required('admisiones.delete_aspirante', raise_exception=True)
def eliminar_aspirante(request, pk):
    aspirante = get_object_or_404(Aspirante, pk=pk)

    if request.method == 'POST':
        aspirante.delete()
        return redirect('listar_aspirantes')

    return render(
        request,
        'admisiones/aspirantes/eliminar.html',
        {'aspirante': aspirante}
    )
