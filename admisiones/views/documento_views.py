
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from admisiones.models import Documento
from admisiones.forms import DocumentoForm


@login_required(login_url='login')
@permission_required('admisiones.view_documento', raise_exception=True)
def listar_documentos(request):
    documentos = Documento.objects.all()

    return render(
        request,
        'admisiones/documentos/listar.html',
        {'documentos': documentos}
    )


@login_required(login_url='login')
@permission_required('admisiones.add_documento', raise_exception=True)
def crear_documento(request):
    if request.method == 'POST':
        formulario = DocumentoForm(request.POST, request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_documentos')
    else:
        formulario = DocumentoForm()

    return render(
        request,
        'admisiones/documentos/formulario.html',
        {'formulario': formulario}
    )
