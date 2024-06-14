from django.contrib import admin

# model
from .models import RegisterUser, Profile
from job.models import SavedJob


from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django.contrib.auth.forms import UserChangeForm


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()
    class Meta(UserChangeForm.Meta):
        model = RegisterUser




class RegisterUserAdmin(admin.ModelAdmin):
    search_fields = ["id", "first_name", "username"]
    list_display = ["id", "username", "first_name", "last_name", "email"]


admin.site.register(RegisterUser, RegisterUserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ["id", "user","group"]
    list_display = ["user","group"]


admin.site.register(Profile, ProfileAdmin)

class SavedJobAdmin(admin.ModelAdmin):
    search_fields = ["id", ]
    list_display = ("id", "user", "job")


admin.site.register(SavedJob, SavedJobAdmin)
