from django.contrib import admin

# model
from .models import Job


class JobAdmin(admin.ModelAdmin):
    search_fields = ["id", "title", "company","user"]
    list_display = ["id", "title", "company","user"]


admin.site.register(Job, JobAdmin)

