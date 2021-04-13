from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404



def index(request):
    # подключаем HTML шаблон для главной страницы
    if request.user.is_authenticated:
        return render(request, 'files_manager/index.html')
    else:
        return redirect('login')



# def new_files(request):
#     # подключаем HTML шаблон для главной страницы
#     return render(request, 'files_manager/new_files.html')


def new_files(request):
    if request.user.is_authenticated:
        posts = []
        for i in Post.objects.all():
            if i.stage == "new_files":
                posts.append(i)
        data = {
            'values': {'on': "on_check", 'in': "in_work", 'ou': "outdated"},
            'title': 'Post Page',
            'posts': posts
        }
        return render(request, 'files_manager/new_files.html', data)
    else:
        return redirect('login')


def on_check(request):
    # подключаем HTML шаблон для главной страницы
    if request.user.is_authenticated:
        posts = []
        for i in Post.objects.all():
            if i.stage == "on_check":
                posts.append(i)
        data = {
            'values': {'on': "on_check", 'in': "in_work", 'ou': "outdated"},
            'title': 'Post Page',
            'posts': posts
        }
        return render(request, 'files_manager/on_check.html', data)
    else:
        return redirect('login')



def in_work(request):
    # подключаем HTML шаблон для главной страницы
    if request.user.is_authenticated:
        posts = []
        for i in Post.objects.all():
            if i.stage == "in_work":
                posts.append(i)
        data = {
            'values': {'on': "on_check", 'in': "in_work", 'ou': "outdated"},
            'title': 'Post Page',
            'posts': posts
        }
        return render(request, 'files_manager/in_work.html', data)
    else:
        return redirect('login')



def outdated(request):
    if request.user.is_authenticated:
        posts = []
        for i in Post.objects.all():
            if i.stage == "outdated":
                posts.append(i)
        data = {
            'values': {'on': "on_check", 'in': "in_work", 'ou': "outdated"},
            'title': 'Post Page',
            'posts': posts
        }
        return render(request, 'files_manager/outdated.html', data)
    else:
        return redirect('login')



# ---- для выгрузки файлов ---------------------------
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "files_manager/post.html"
    success_url = reverse_lazy("new_files")
# -----------------------------------------------------
# -------------------DELETE FILE ----------------------
def delete_f(request, pk):
    if request.method == "POST":
        file = Post.objects.get(pk=pk)
        file.delete()
    return redirect(request.META.get('HTTP_REFERER'))
# -----------------------------------------------------
# -----------------MOV FILE---------------------------
    # file = get_object_or_404(Post, pk=pk)
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     form.save()
    # return redirect(request.META.get('HTTP_REFERER'))


def move_to(request, pk):
    urls = request.get_full_path().split("/")
    get_artikles = Post.objects.get(pk=pk)
    if request.method == "POST":
        get_artikles.stage = urls[1][8::]
        get_artikles.save()
    return redirect(request.META.get('HTTP_REFERER'))
# ------------------------------------------------------





