# Generated by Django 5.0.7 on 2024-07-16 18:56

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=50, verbose_name='Имя питомца')),
                ('type', models.CharField(choices=[('DOG', 'dog'), ('CAT', 'cat')], max_length=50, verbose_name='Вид')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи')),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(50, message='Возраст питомца, к сожалению, не может быть больше 50.')], verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото питомца')),
                ('url', models.CharField(max_length=50, verbose_name='URL фото')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='pets.pet', verbose_name='Питомец')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
                'ordering': ('pet__name',),
            },
        ),
    ]