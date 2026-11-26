
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from admisiones.forms import RegistroForm


def registrar_usuario(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)

        if formulario.is_valid():
            usuario = formulario.save()

            asesores, creado = Group.objects.get_or_create(
                name='Asesores'
            )

            usuario.groups.add(asesores)

            login(request, usuario)
            return redirect('listar_aspirantes')
    else:
        formulario = RegistroForm()

    return render(
        request,
        'admisiones/auth/registro.html',
        {'formulario': formulario}
    )


def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect('listar_aspirantes')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        formulario = AuthenticationForm()

    return render(
        request,
        'admisiones/auth/login.html',
        {'formulario': formulario}
    )


def cerrar_sesion(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    return redirect('listar_aspirantes')
