from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Pet, PetPhoto


class PetPhotoInline(admin.TabularInline):
    model = PetPhoto
    min_num = 1


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
