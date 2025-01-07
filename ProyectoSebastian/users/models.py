from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')  # Relaciona el avatar con un usuario
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Campo para cargar la imagen del avatar

    def __str__(self):
        return f"{self.user.username}'s Avatar"