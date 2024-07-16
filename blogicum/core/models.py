from django.db import models


class BaseModel(models.Model):
    """Базовая абстрактная модель."""

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено'
    )
    

    class Meta:
        abstract = True
        verbose_name = 'Базовая модель'


    def __str__(self):
        return self.title
        