from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True) # Идентификатор
    username = models.CharField(max_length=50, unique=True) # Логин
    password = models.CharField(max_length=50)# False
    email = models.EmailField(max_length=100, unique=True) # Email
    is_active = models.BooleanField(default=True) # Статус активации
    is_staff = models.BooleanField(default=False) # Статус админа

    # Метод для отображения в админ панели
    def __str__(self):
        return self.email