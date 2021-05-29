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
from .views import CreatePostView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main_page', views.index, name='main_page'),
    path('task_manager', include('task_manager.urls'),name='task_manger'),
    path('new_files', views.new_files, name='new_files'),
    path('on_check', views.on_check, name='on_check'),
    path('in_work', views.in_work, name='in_work'),
    path('outdated', views.outdated, name='outdated'),
    path('users_list', include('users.urls'), name='user_list'),
    # -------- для выгрзки файлов ----------------------------
    path('post', CreatePostView.as_view(), name='post'),
    # -------- Delete File -----------------------------------
    path('new_files/<int:pk>', views.delete_f, name='delete_f'),
    # -------- Move File -------------------------------------
    path('move_to_new_files/<int:pk>', views.move_to, name='move_to_new_files'),
    path('move_to_on_check/<int:pk>', views.move_to, name='move_to_on_check'),
    path('move_to_in_work/<int:pk>', views.move_to, name='move_to_in_work'),
    path('move_to_outdated/<int:pk>', views.move_to, name='move_to_outdated'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
