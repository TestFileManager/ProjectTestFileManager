from django.contrib import admin

# ---обновим файл posts/admin.py, после чего в Django ---------------------
# появится возможность использовать приложение Post от имени администратора.

from .models import Post



admin.site.register(Post)
