
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Crea los grupos y asigna sus permisos'

    def handle(self, *args, **kwargs):
        modelos = [
            'aspirante',
            'carrera',
            'solicitud',
            'documento',
        ]

        permisos = Permission.objects.filter(
            content_type__app_label='admisiones',
            content_type__model__in=modelos
        )

        administradores, _ = Group.objects.get_or_create(
            name='Administradores'
        )

        asesores, _ = Group.objects.get_or_create(
            name='Asesores'
        )

        # Administradores: todos los permisos
        administradores.permissions.set(permisos)

        # Asesores: consultar, crear y editar
        permisos_asesores = permisos.exclude(
            codename__startswith='delete_'
        )

        asesores.permissions.set(permisos_asesores)

        self.stdout.write(
            self.style.SUCCESS(
                'Grupos y permisos configurados correctamente.'
            )
        )
