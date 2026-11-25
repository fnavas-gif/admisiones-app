
from django import forms
from admisiones.models import Documento


class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento

        fields = [
            'solicitud',
            'tipo',
            'archivo',
            'estado',
            'fecha_entrega',
            'observaciones',
        ]

        widgets = {
            'fecha_entrega': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
            'observaciones': forms.Textarea(
                attrs={'rows': 3}
            ),
        }

        labels = {
            'solicitud': 'Solicitud de admisión',
            'tipo': 'Tipo de documento',
            'archivo': 'Seleccionar archivo',
            'estado': 'Estado del documento',
            'fecha_entrega': 'Fecha de entrega',
            'observaciones': 'Observaciones',
        }