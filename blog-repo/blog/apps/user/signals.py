from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from apps.user.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_groups_and_permissions(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        try:
            #TODO=definir los permisos de post y de comments

            #Crear grupos de usuarios registrados
            registered_group, created = Group.objects.get_or_create(
                name="Registered"
            )
            registered_group.permissions.add(
                #permiso para ver post
                #permiso para ver comentarios del post
                #permiso para crear comentarios del post
                #permiso para actualizar su comentario en un post
                #permiso para borrar su comentario en un post
            )

            #Crear grupos de usuarios colaboradores
            registered_group, created = Group.objects.get_or_create(
                name="Collaborators"
            )
            registered_group.permissions.add(
                #permiso para ver post
                #permiso para crear post
                #permiso para actualizar su post
                #permiso para borrar post
                #permiso para ver comentarios del post
                #permiso para crear comentarios del post
                #permiso para actualizar su comentario en un post
                #permiso para borrar su comentario en un post
            )
        
            #Crear grupos de usuarios administradores
            registered_group, created = Group.objects.get_or_create(
                name="Admins"
            )
            registered_group.permissions.add(
                #permiso para ver post
                #permiso para crear post
                #permiso para actualizar su post
                #permiso para borrar cualquier post
                #permiso para ver comentarios del post
                #permiso para crear comentarios del post
                #permiso para actualizar su comentario en un post
                #permiso para borrar su comentario en un post
            )

            print("Grupos y permisos creados exitosamente.")
        except ContentType.DoesNotExist:
            print("El tipo aun no se encuentra disponible.")
        except Permission.DoesNotExist:
            print("Uno o mas permisos no se encuentran disponibles.")
            