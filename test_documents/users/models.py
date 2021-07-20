from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)  # Логин
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)  # Email
    is_active = models.BooleanField(default=True)  # Статус активации
    is_staff = models.BooleanField(default=False)  # Статус админа
    role_name = models.ForeignKey(Role, null=False, on_delete=models.CASCADE)

    # Метод для отображения в админ панели
    def __str__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=20)
    team_lead_id = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

