from django.db import models


# Create your models here.
# ------ модель для загрузки файлов ----------

class Post(models.Model):
    comment = models.CharField(max_length=200)
    upload = models.FileField(upload_to="file_manager_upload/")

# ----------- Move --------------------------------
    stage = models.CharField(max_length=200, default="new_files")

    def get_absolute_url(self):
        return '/new_files'
# -------- Delete file ----------------------------

def delete(self, *args, **kwargs):
    self.upload.delete()
    super().delete(*args, **kwargs)
# --------------------------------------------------

def __str__(self):
    return self.comment


# Меняем название таблицы в Админ Панеле
class Meta:
    verbose_name = 'Файл'
    verbose_name_plural = 'Файлы'
# ----------------------------------------------
