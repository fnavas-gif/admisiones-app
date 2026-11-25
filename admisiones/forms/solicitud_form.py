
from django import forms
from admisiones.models import Solicitud


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
            'aspirante',
            'carrera',
            'estado',
            'observaciones',
        ]

        widgets = {
            'observaciones': forms.Textarea(
                attrs={'rows': 3}
            ),
        }

        labels = {
            'aspirante': 'Seleccionar aspirante',
            'carrera': 'Carrera solicitada',
            'estado': 'Estado de la solicitud',
            'observaciones': 'Observaciones',
        }