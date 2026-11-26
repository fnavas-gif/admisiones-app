
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from admisiones.models import Solicitud
from admisiones.forms import SolicitudForm


@login_required(login_url='login')
@permission_required('admisiones.view_solicitud', raise_exception=True)
def listar_solicitudes(request):
    solicitudes = Solicitud.objects.all()

    return render(
        request,
        'admisiones/solicitudes/listar.html',
        {'solicitudes': solicitudes}
    )


@login_required(login_url='login')
@permission_required('admisiones.add_solicitud', raise_exception=True)
def crear_solicitud(request):
    if request.method == 'POST':
        formulario = SolicitudForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_solicitudes')
    else:
        formulario = SolicitudForm()

    return render(
        request,
        'admisiones/solicitudes/formulario.html',
        {'formulario': formulario}
    )