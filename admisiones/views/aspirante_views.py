from django.shortcuts import render, redirect, get_object_or_404
from admisiones.models import Aspirante
from admisiones.forms import AspiranteForm


def listar_aspirantes(request):
    aspirantes = Aspirante.objects.all()

    return render(
        request,
        'admisiones/aspirantes/listar.html',
        {'aspirantes': aspirantes}
    )


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


def detalle_aspirante(request, pk):
    aspirante = get_object_or_404(Aspirante, pk=pk)

    return render(
        request,
        'admisiones/aspirantes/detalle.html',
        {'aspirante': aspirante}
    )