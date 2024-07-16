from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """Базовая абстрактная модель."""

    is_published = models.BooleanField(
        default=True,
        blank=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        verbose_name='Добавлено',
        help_text='Время создания записи'
    )

    class Meta:
        abstract = True
        verbose_name = 'Базовая модель'

    def __str__(self):
        return self.title


class TSPdModel(BaseModel):
    """TSPd - Title Slug Pub_date абстрактная модель"""

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name='Заголовок'
    )

    slug = models.SlugField(
        max_length=64,
        blank=True,
        unique=False,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы,'
        ' цифры, дефис и подчёркивание.'
    )

    pub_date = models.DateTimeField(
        default=timezone.now,
        auto_now=False,
        blank=False,
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — можно делать'
        ' отложенные публикации.'
    )

    class Meta:
        abstract = True
        verbose_name = 'tspd модель'
