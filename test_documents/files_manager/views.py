from django.shortcuts import render

# Create your views here.


def index(request):
    # подключаем HTML шаблон для главной страницы
    return render(request, 'files_manager/index.html')


def new_files(request):
    # подключаем HTML шаблон для главной страницы
    return render(request, 'files_manager/new_files.html')


def on_check(request):
    # подключаем HTML шаблон для главной страницы
    return render(request, 'files_manager/on_check.html')


def in_work(request):
    # подключаем HTML шаблон для главной страницы
    return render(request, 'files_manager/in_work.html')


def outdated(request):
    # подключаем HTML шаблон для главной страницы
    return render(request, 'files_manager/outdated.html')
