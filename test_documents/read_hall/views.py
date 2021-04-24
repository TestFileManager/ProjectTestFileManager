from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book

# Create your views here.

# ---- книги на сервер ---------------------------


class BookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "read_hall/add_book.html"
    success_url = reverse_lazy("home")
# -----------------------------------------------------
# -----------Общий обзор книги-------------------------


class BookDetail(DetailView):
    model = Book
    template_name = "read_hall/book_detail.html"
    context_object_name = 'book'


def r_h_i(request):
    # подключаем HTML шаблон для главной страницы
    if request.user.is_authenticated:
        books = Book.objects.all()
        data = {
            "book": books
        }
        return render(request, 'read_hall/read_hall.html', data)
    else:
        return redirect('login')


def add_book(request):
    return render(request, 'read_hall/add_book.html')
# ---------- Удаление книги ----------------


def delete_book(request, tk):
    if request.method == "POST":
        book = Book.objects.get(pk=tk)
        book.delete()
        book.deletes()
    return redirect('home')
# ------- Прочтение книги ----------------


def read_book(request, rk):
    if request.method == "POST":
        book = Book.objects.get(pk=rk)
        a = book.file.url
        print(a)

