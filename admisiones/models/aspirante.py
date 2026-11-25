
from django.db import models


class Aspirante(models.Model):

    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()

    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        ordering = ['apellidos', 'nombres']
        verbose_name = 'Aspirante'
        verbose_name_plural = 'Aspirantes'