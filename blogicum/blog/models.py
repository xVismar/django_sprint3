from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel
from core.models import TSPdModel
from django.template.defaultfilters import truncatewords

User = get_user_model()

# core.models.TSPdModel(BaseModel) передаёт:
# text
# slug
# pub_date
#
# Наследует от BaseModel:
# created_at
# is_published


class Post(TSPdModel):
    # Функция - обрезаем текст по 10 слов для дисплея в админке.
    def short_text(self):
        return truncatewords(self.text, 10)

    text = models.TextField(verbose_name='Текст')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации'

    )

    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Местоположение'
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)


class Category(TSPdModel):
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        max_length=64,
        unique=True,
        blank=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы,'
        ' цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        ordering = ('-pub_date',)


class Location(BaseModel):
    name = models.CharField(
        max_length=256,
        verbose_name='Название места'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name
