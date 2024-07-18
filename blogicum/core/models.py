from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """Базовая абстрактная модель."""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
        help_text='Время создания записи.'
    )

    class Meta:
        abstract = True
        verbose_name = 'Базовая модель'


class PdModel(BaseModel):
    """Pub_date абстрактная модель, дополняет BaseModel."""

    pub_date = models.DateTimeField(
        default=timezone.now(),
        auto_now=False,
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — можно делать'
        ' отложенные публикации.'
    )

    class Meta:
        abstract = True
        verbose_name = 'pub_date модель'

    def __str__(self):
        return self.title
