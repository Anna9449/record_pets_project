from django_filters import BooleanFilter, FilterSet

from pets.models import Pet


class PetFilter(FilterSet):
    """
    Кастомный фильтр, если в параметрах передается поле has_photos,
    осуществляется фильтрация по записям о питомцах:
        has_photos = True - выводятся все записи с фото
        has_photos = False - выводятся все записи без фото
    """
    has_photos = BooleanFilter(method='filter_has_photos')

    class Meta:
        model = Pet
        fields = ('has_photos',)

    def filter_has_photos(self, queryset, name, value):
        if value:
            return queryset.exclude(photos=None)
        return queryset.filter(photos=None)
