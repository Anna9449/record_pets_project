from http import HTTPStatus

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .filters import PetFilter
from .pagination import CustomPagination
from .serializers import (PetSerializer, PetDeleteSerializer,
                          PetDeleteResponseSerializer, PetPhotoSerializer)
from .schema import response_400, response_401
from pets.models import Pet


@extend_schema_view(
    create=extend_schema(
        summary='api/pets/ создание записи о питомце',
        description='Создание записи о питомце.',
        responses={
            201: PetSerializer,
            400: response_400,
            401: response_401
        }
    ),
    list=extend_schema(
        summary='api/pets/ получение списка питомцев',
        description='Получение списка питомцев.',
        responses={
            200: PetSerializer,
            401: response_401
        }
    ),
    destroy=extend_schema(
        summary='api/pets/ удаление записей о питомцах списком',
        responses={
            204: PetDeleteResponseSerializer,
            400: response_400,
            401: response_401
        }
    ),
    photo=extend_schema(
        summary='api/pets/{id}/photo/ добавление фото питомца',
        methods=('POST',),
        responses={
            201: PetPhotoSerializer,
            400: response_400,
            401: response_401
        }
    )
)
class PetViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """
    Вьюсет:
        - создания записи о питомце,
        - получения списка записей,
        - добавления фото питомца,
        - удаления списка записей о питомцах.
    """
    queryset = Pet.objects.prefetch_related('photos')
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PetFilter

    def get_serializer_class(self):
        if self.action == 'destroy':
            return PetDeleteSerializer
        elif self.action == 'photo':
            return PetPhotoSerializer
        return PetSerializer

    def destroy(self, request, *args, **kwargs):
        """
        Метод принимает список id питомцев в формате:
        "ids": ["id_питомца1", "id_питомца2", ...]
        """

        serializer = PetDeleteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_list = request.data['ids']
        obj_list = Pet.objects.filter(id__in=id_list)
        for obj in obj_list:
            id_list.remove(obj.id)
        for index in range(len(id_list)):
            id_list[index] = {
                'id': id_list[index],
                'error': 'Pet with the matching ID was not found'
            }
        count_obj_del = obj_list.count()
        obj_list.delete()
        return Response(
            data={'deleted': count_obj_del,
                  'errors': id_list},
            status=HTTPStatus.NO_CONTENT
        )

    @action(methods=('POST',),
            detail=True, url_path='photo')
    def photo(self, request, pk):
        """
        Метод принимает фото питомца формата form-data.
        """

        pet = get_object_or_404(Pet, pk=pk)
        serializer = self.get_serializer(
            data=request.data,
            context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(pet=pet)
        return Response(serializer.data, status=HTTPStatus.CREATED)
