from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        # Название формы с которой работаем
        model = Task
        # Какие поля должны присутствовать в самой форме
        fields = ["title", "task"]
        # Обьединение красоты и функциональности полей
        # attrs - atributes
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Название задачи'
            }),
            "task": Textarea(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Описание задачи',
                'rows': 10
            })
        }