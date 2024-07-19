import logging
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import PetPhoto


@receiver(post_delete, sender=PetPhoto)
def delete_photo_file(sender, instance, **kwargs):
    """
    Сигнал, отслеживает удаление объектов из модели PetPhoto
    и удаляет файл фотографии из папки.
    """

    url = instance.photo.path
    logging.info(f'Попытка удалить фото {url}')
    if os.path.exists(url):
        os.remove(url)
    print('Фото удалено')
    logging.info('Фото удалено')
