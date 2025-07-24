from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
import os

def get_avatar_filename(instance, filename):
    # avatar_default.jpm
    # avatar_default   .jpg
    base_filename, file_extension = os.path.splitext(filename)
    new_filename = f'user_{instance.id}_acatar{file_extension}'
    return os.path.join('user/avatar/', new_filename)

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to=get_avatar_filename, default='user/default/avatar_default.jpg')

    def __str__(self):
        return self.username

    @property
    def is_registered(self):
        return self.groups.filter(name="Registered").exists()

    @property
    def is_collaborator(self):
        return self.groups.filter(name="Collaborators").exists()
    
    @property
    def is_admin(self):
        return self.groups.filter(name="Admins").exists()




