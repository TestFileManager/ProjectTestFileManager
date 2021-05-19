from django.db import models

# Create your models here.
# ------- Модель книги -------------------


class Book(models.Model):
    name = models.CharField('Название книги', max_length=200)
    short_description = models.CharField('Краткое описание', max_length=500)
    description = models.TextField('Описание')
    cover = models.FileField('Обложка', upload_to="file_read_hall/cover/")
    file = models.FileField('Книга', upload_to="file_read_hall/")
    author = models.CharField('Автор', max_length=200,default="unknown")

    def deletes(self, *args, **kwargs):
        self.file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/read_hall/{self.id}'


class Meta:
    verbose_name = 'Книга'
    verbose_name_plural = 'Книги'
# -----------------------------------------


