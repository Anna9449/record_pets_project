from rest_framework import serializers

from pets.models import Pet, PetPhoto


class PetPhotoSerializer(serializers.ModelSerializer):
    """
    Сериализатор загрузки(создания) фото и вывода информации о фото питомца.
    """

    url = serializers.ImageField(source='photo', read_only=True, use_url=True)
    photo = serializers.ImageField(use_url=False, write_only=True)

    class Meta:
        model = PetPhoto
        fields = ('id', 'photo', 'url')


class PetSerializer(serializers.ModelSerializer):
    """
    Сериализатор создания записи о питомце и вывода списка записей о питомцах.
    """

    photos = PetPhotoSerializer(many=True, read_only=True)
    type = serializers.CharField(source='get_type_display', read_only=True)
    type_name = serializers.CharField(source='type', write_only=True)

    class Meta:
        model = Pet
        fields = (
            'id', 'name', 'age', 'type', 'type_name', 'photos', 'created_at'
        )


class PetDeleteSerializer(serializers.Serializer):
    """
    Сериализатор проверки формата запроса на удаление записей о питомцах.
    """

    ids = serializers.ListField(child=serializers.UUIDField())


class PetDeleteErrSerializer(serializers.Serializer):
    """
    Сериализатор вывода ошибки удаления записи о питомце - для документации.
    """

    id = serializers.UUIDField()
    error = serializers.CharField()


class PetDeleteResponseSerializer(serializers.Serializer):
    """
    Сериализатор вывода общей информации об удалении записией о питомцах
     - для документации.
    """

    deleted = serializers.IntegerField()
    errors = PetDeleteErrSerializer(many=True)
