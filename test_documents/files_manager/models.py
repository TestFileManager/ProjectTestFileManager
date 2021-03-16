from django.db import models

# Create your models here.
# ------ модель для загрузки файлов ----------
class Post(models.Model):
    comment = models.CharField(max_length= 200, null=True)
    upload = models.FileField(upload_to="file_manager_upload/")

#-------- Delete file ----------------------------
    def delete(self,*args,**kwargs):
        self.upload.delete()
        super().delete(*args,**kwargs)
# --------------------------------------------------
    def __str__(self):
        return self.comment

    # Меняем название таблицы в Админ Панеле
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
# ----------------------------------------------
