from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post
from django.contrib.auth import authenticate, login, logout



def index(request):
    # подключаем HTML шаблон для главной страницы
    if request.user.is_authenticated:
        return render(request, 'files_manager/index.html')
    else:
        return redirect('login')



# def new_files(request):
#     # подключаем HTML шаблон для главной страницы
#     return render(request, 'files_manager/new_files.html')


def on_check(request):
    # подключаем HTML шаблон для главной страницы
    if request.user.is_authenticated:
        return render(request, 'files_manager/on_check.html')
    else:
        return redirect('login')



def in_work(request):
    # подключаем HTML шаблон для главной страницы
    if request.user.is_authenticated:
        return render(request, 'files_manager/in_work.html')
    else:
        return redirect('login')



def outdated(request):
    if request.user.is_authenticated:
        return render(request, 'files_manager/outdated.html')
    else:
        return redirect('login')



# ---- для выгрузки файлов ---------------------------

class HomePageView(ListView):
    model = Post
    template_name = "files_manager/post.html"


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "files_manager/post.html"
    success_url = reverse_lazy("new_files")
# -----------------------------------------------------

def new_files(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'files_manager/new_files.html', {'title': 'Post Page', 'posts': posts})
    else:
        return redirect('login')




