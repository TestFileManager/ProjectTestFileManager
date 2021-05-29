from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True, unique=True)  # Идентификатор
    username = models.CharField(max_length=50, unique=True)  # Логин
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)  # Email
    is_active = models.BooleanField(default=True)  # Статус активации
    is_staff = models.BooleanField(default=False)  # Статус админа

    # Метод для отображения в админ панели
    def __str__(self):
        return self.id


class Role(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.id


class RoleUsers(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user_id = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Team(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    team_lead_id = models.IntegerField()

    def __str__(self):
        return self.id


class TeamUsers(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
