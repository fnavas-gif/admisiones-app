
from django.db import models


class Documento(models.Model):

    class TipoDocumento(models.TextChoices):
        CEDULA = 'CEDULA', 'Copia de cédula'
        TITULO = 'TITULO', 'Título de bachiller'
        VOTACION = 'VOTACION', 'Certificado de votación'
        FOTO = 'FOTO', 'Fotografía'
        OTRO = 'OTRO', 'Otro'

    class Estado(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        ENTREGADO = 'ENTREGADO', 'Entregado'
        RECHAZADO = 'RECHAZADO', 'Rechazado'

    solicitud = models.ForeignKey(
        'admisiones.Solicitud',
        on_delete=models.CASCADE,
        related_name='documentos'
    )

    tipo = models.CharField(
        max_length=12,
        choices=TipoDocumento.choices
    )

    archivo = models.FileField(
        upload_to='documentos_admision/',
        blank=True,
        null=True
    )

    estado = models.CharField(
        max_length=12,
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )

    fecha_entrega = models.DateTimeField(
        blank=True,
        null=True
    )

    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.solicitud}"

    class Meta:
        ordering = ['tipo']
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'