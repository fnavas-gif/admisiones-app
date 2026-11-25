
from django.db import models


class Carrera(models.Model):

    class Modalidad(models.TextChoices):
        PRESENCIAL = 'PRESENCIAL', 'Presencial'
        VIRTUAL = 'VIRTUAL', 'Virtual'
        HIBRIDA = 'HIBRIDA', 'Híbrida'

    nombre = models.CharField(max_length=120, unique=True)
    codigo = models.CharField(max_length=15, unique=True)
    descripcion = models.TextField(blank=True)
    duracion_semestres = models.PositiveSmallIntegerField(default=5)

    modalidad = models.CharField(
        max_length=12,
        choices=Modalidad.choices,
        default=Modalidad.PRESENCIAL
    )

    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
