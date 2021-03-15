from django.db import models

# Create your models here.
# ------ модель для загрузки файлов ----------
class Post(models.Model):
    title = models.TextField()
    cover = models.FileField(upload_to="file_manager_upload/")

    def __str__(self):
        return self.title

    # Меняем название таблицы в Админ Панеле
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
# ----------------------------------------------
