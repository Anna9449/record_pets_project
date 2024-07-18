from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Pet, PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'pet'
    )
    search_fields = ('pet',)


class PetPhotoInline(admin.TabularInline):
    model = PetPhoto
    extra = 1


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type',
        'age',
        'created_at',
    )
    list_filter = ('type',)
    search_fields = ('name',)
    inlines = (PetPhotoInline,)


admin.site.unregister(Group)
