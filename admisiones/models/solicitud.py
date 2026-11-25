
from django.db import models


class Solicitud(models.Model):

    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        EN_REVISION = 'EN_REVISION', 'En revisión'
        APROBADA = 'APROBADA', 'Aprobada'
        RECHAZADA = 'RECHAZADA', 'Rechazada'

    aspirante = models.ForeignKey(
        'admisiones.Aspirante',
        on_delete=models.CASCADE,
        related_name='solicitudes'
    )

    carrera = models.ForeignKey(
        'admisiones.Carrera',
        on_delete=models.PROTECT,
        related_name='solicitudes'
    )

    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    estado = models.CharField(
        max_length=12,
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )

    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Solicitud {self.id} - {self.aspirante}"

    class Meta:
        ordering = ['-fecha_solicitud']
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'