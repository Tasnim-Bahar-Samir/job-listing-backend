from django.db import models

#models
from user.models import RegisterUser

# utils

import uuid


JOB_TYPES = [
    ("PART_TIME", "Part Time"),
    ("FULL_TIME", "Full Time"),
    ("INTERNSHIP", "Internship"),
]

# Create your models here.

class Job(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    user = models.ForeignKey(
        RegisterUser, related_name="job_user", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=25, default='FULL_TIME', choices=JOB_TYPES)
    company = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    salary = models.CharField(max_length=255, null=True)
    deadline = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class SavedJob(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    user = models.ForeignKey(
        RegisterUser, related_name="user", on_delete=models.CASCADE
    )
    job = models.ForeignKey(
        Job, related_name="saved_job", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)