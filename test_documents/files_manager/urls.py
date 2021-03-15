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
from django.urls import path, include
from . import views
from .views import HomePageView, CreatePostView

urlpatterns = [
    path('main_page', views.index, name='main_page'),
    path('task_manager', include('task_manager.urls'), name='task_manager'),
    path('new_files', views.new_files, name='new_files'),
    path('on_check', views.on_check, name='on_check'),
    path('in_work', views.in_work, name='in_work'),
    path('outdated', views.outdated, name='outdated'),
    # -------- для выгрзки файлов ----------------------------
    path('post', CreatePostView.as_view(), name='post')
    # ---------------------------------------------------------
]
