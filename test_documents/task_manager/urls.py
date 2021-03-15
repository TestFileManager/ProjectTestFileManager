from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('task_manager', views.task, name='task'),
    path('create_task', views.create_task, name='create_task')
]