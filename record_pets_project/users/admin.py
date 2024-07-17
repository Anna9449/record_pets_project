from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import PetsProjectUser


@admin.register(PetsProjectUser)
class UserAdmin(BaseUserAdmin):
    pass
