import uuid
from django.core.validators import MaxValueValidator
from django.db import models

from .const import PET_TYPE_CHOICES, MAX_LENGTH_NAME, MAX_LENGTH, MAX_VALUE


class Pet(models.Model):
    """Модель питомца."""

    id = models.UUIDField('id',
                          primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name = models.CharField('Имя питомца',
                            max_length=MAX_LENGTH_NAME)
    type = models.CharField('Вид',
                            choices=PET_TYPE_CHOICES,
                            max_length=MAX_LENGTH)
    created_at = models.DateTimeField('Дата и время создания записи',
                                      auto_now_add=True)
    age = models.PositiveSmallIntegerField(
        'Возраст',
        validators=[
            MaxValueValidator(
                MAX_VALUE,
                message='Возраст питомца, к сожалению, не может быть больше'
                        f' {MAX_VALUE}.'
            ),
        ],
    )

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
        ordering = ('name',)

    def __str__(self):
        return self.name


class PetPhoto(models.Model):
    """Модель фото питомца."""

    id = models.UUIDField('id',
                          primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name='Питомец'
    )
    photo = models.ImageField('Фото питомца',
                              blank=True,
                              null=True)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ('pet__name',)

    def __str__(self):
        return self.pet.name
