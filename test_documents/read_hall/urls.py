"""test_documents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import BookView

# -- для выгрузки файлов -----------------------------
from django.conf import settings
from django.conf.urls.static import static
# -----------------------------------------------------

urlpatterns = [
    path('', views.r_h_i, name='home'),
    path('add_book', BookView.as_view(), name='add_book'),
    path('<int:pk>', views.BookDetail.as_view(), name='book_detail'),
    path('book_detail/<int:tk>', views.delete_book, name='delete_book'),
    path('book_detail/<int:rk>', views.read_book, name='read_book'),
    path('<int:pk>/update_book', views.Update_Book.as_view(), name='update_book'),
]

# -----------------------------------------------------
