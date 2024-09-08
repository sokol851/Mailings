import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=150, default='Не указано', verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=150, default='Не указано', verbose_name='Фамилия', **NULLABLE)

    is_active = models.BooleanField(default=False)
    token_verify = models.UUIDField(default=uuid.uuid4, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
