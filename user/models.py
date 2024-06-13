from django.db import models
from django.contrib.auth.models import AbstractUser

#utils
import uuid

#models
from auth0.models import Group

# Create your models here.

class RegisterUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    email = models.EmailField(unique=True)


class Profile(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    user = models.OneToOneField(
        RegisterUser, related_name="user_profile", on_delete=models.CASCADE
    )
    group = models.ManyToManyField(Group, blank=True, related_name='group')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user)
    
    