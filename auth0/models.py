from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GROUPS = [
    ('CANDIDATE', 'Candidate'),
    ('COMPANY', 'Company'),
]

class Group(models.Model):
    group_title = models.CharField(max_length=20, choices=GROUPS, default="CANDIDATE")
    
    def __str__(self):
        return self.group_title