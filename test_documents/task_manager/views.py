from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def task(request):
    if request.user.is_authenticated:
        tasks = Task.objects.all()
        return render(request, 'task_manager/task.html', {'title': 'Task Page', 'tasks': tasks})
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('error_login_page')


def create_task(request):
    #переменная для ошибки
    error = ''
    #Отслеживать добавление данных в БД
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            #переадресация на страницу с тасками
            return redirect('task')
        #если форма не кореектная то ошибку выбивать будет
        else:
            error = 'error'
    #Подключаем обработчик формы на нашу страницу
    form = TaskForm()
    create_tasks = {
        'form': form,
        'error': error
    }
    #Возвращаем на нашу страницу шаблон и обработчик формы
    return render(request, 'task_manager/create_task.html', create_tasks)