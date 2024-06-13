from django.db import models


# utils
# from django_resized import ResizedImageField
# from ckeditor.fields import RichTextField

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
    title = models.CharField(max_length=255, null=True, unique=True)
    type = models.CharField(max_length=25, default='FULL_TIME', choices=JOB_TYPES)
    company = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    deadline = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
