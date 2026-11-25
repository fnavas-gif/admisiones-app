
from django import forms
from admisiones.models import Aspirante


class AspiranteForm(forms.ModelForm):

    class Meta:
        model = Aspirante

        fields = [
            'cedula',
            'nombres',
            'apellidos',
            'correo',
            'telefono',
            'fecha_nacimiento',
            'direccion',
        ]

        widgets = {
            'fecha_nacimiento': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'direccion': forms.Textarea(
                attrs={'rows': 3}
            ),
        }

        labels = {
            'cedula': 'Número de cédula',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'correo': 'Correo electrónico',
            'telefono': 'Teléfono',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'direccion': 'Dirección domiciliaria',
        }