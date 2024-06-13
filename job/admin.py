from django.contrib import admin

# model
from .models import Job


class JobAdmin(admin.ModelAdmin):
    search_fields = ["id", "title", "company"]
    list_display = ["id", "title", "company"]


admin.site.register(Job, JobAdmin)

