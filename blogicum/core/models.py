from django.db import models


class BaseModel(models.Model):
    """Абстрактная модель."""

    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        verbose_name = 'Базовая модель'
