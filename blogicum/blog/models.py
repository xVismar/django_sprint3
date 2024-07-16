from django.db import models # noqa
from django.contrib.auth import get_user_model # noqa
from core.models import BaseModel, TSPdModel
from django.template.defaultfilters import truncatewords

User = get_user_model()

# core.models.TSPdModel передаёт:
# text
# slug
# pub_date
#
# Наследуется от BaseModel:
# created_at
# is_published


class Post(TSPdModel):
    # Функция - обрезаем текст по 10 слов для дисплея в админке.
    def short_text(self):
        return truncatewords(self.text, 10)

    text = models.TextField(verbose_name='Текст', blank=False)

    author = models.ForeignKey(
        User,
        blank=False,
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
        blank=False,
        related_name='posts',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)


class Category(TSPdModel):
    description = models.TextField(blank=False, verbose_name='Описание')
    slug = models.SlugField(
        max_length=64,
        blank=True,
        unique=True,
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
        blank=False,
        verbose_name='Название места'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name
