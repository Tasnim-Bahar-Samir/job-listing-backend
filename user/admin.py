from django.contrib import admin

# model
from .models import RegisterUser, Profile


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
    search_fields = ["id", "user"]
    list_display = ["user"]


admin.site.register(Profile, ProfileAdmin)