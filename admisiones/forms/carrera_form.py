
from django import forms
from admisiones.models import Carrera


class CarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera

        fields = [
            'nombre',
            'codigo',
            'descripcion',
            'duracion_semestres',
            'modalidad',
            'activa',
        ]

        widgets = {
            'descripcion': forms.Textarea(
                attrs={'rows': 3}
            ),
        }

        labels = {
            'nombre': 'Nombre de la carrera',
            'codigo': 'Código de la carrera',
            'descripcion': 'Descripción',
            'duracion_semestres': 'Duración en semestres',
            'modalidad': 'Modalidad de estudio',
            'activa': 'Carrera activa',
        }