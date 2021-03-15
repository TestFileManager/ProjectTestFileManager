from django.shortcuts import render
from .models import Task
from .forms import TaskForm


# Create your views here.
def task(request):
    tasks = Task.objects.all()
    return render(request, 'task_manager/task.html', {'title': 'Task Page', 'tasks': tasks})


def create_task(request):
    #Отслеживать добавление данных в БД
    
    #Подключаем обработчик формы на нашу страницу
    form = TaskForm()
    create_tasks = {
        'form': form
    }
    #Возвращаем на нашу страницу шаблон и обработчик формы
    return render(request, 'task_manager/create_task.html', create_tasks)