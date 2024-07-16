from django.db import models
from django.contrib.auth import get_user_model
from core.models import BaseModel
from datetime import datetime as dt

User = get_user_model()

class Post(BaseModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок', blank=False)
    text = models.TextField(verbose_name='Текст', blank=False)
    slug = models.SlugField(
        max_length=64,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )

    pub_date = models.DateTimeField(
        default=dt.now(),
        auto_now=False,
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — можно делать отложенные публикации.'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации'
    )

    location = models.ForeignKey(
        'Location',
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Местоположение',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Категория',
        null=True,
        blank=False,
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'


class Category(BaseModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(BaseModel):
    name = models.CharField(max_length=256, verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


