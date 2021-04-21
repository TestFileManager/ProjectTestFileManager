from django.db import models

# Create your models here.
# ------- Модель книги -------------------


class Book(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    cover = models.FileField(upload_to="file_read_hall/cover/")
    file = models.FileField(upload_to="file_read_hall/")
    author = models.CharField(max_length=200,default="unknown")

    def deletes(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'Книга'
    verbose_name_plural = 'Книги'
# -----------------------------------------


