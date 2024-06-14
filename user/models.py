from django.db import models
from django.contrib.auth.models import AbstractUser

#models 

#utils
import uuid


GROUPS = [
    ('CANDIDATE', 'Candidate'),
    ('COMPANY', 'Company'),
]

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
    group = models.CharField(max_length=25, choices=GROUPS, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user)
    
    