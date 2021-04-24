# --- для выгрузки файлов ---------------
from django import forms
from .models import Book
from django.forms import FileInput, TextInput, Textarea
# -----------Форма с книгами----------


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name', 'short_description', 'description',
            'cover', 'file', 'author'
                 ]
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Название книги',
            }),
            'short_description': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Краткое описание'
            }),
            'description': Textarea(attrs={
                'class': "form-control",
                'rows': "3",
                'placeholder': 'Описание'
            }),
            'author': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Автор'
            }),
            'file': FileInput(attrs={
                'class': "form-control input-sm",

                'placeholder': 'Книга'
            }),
            'cover': FileInput(attrs={
                'class': "form-control input-sm",
                'id': "formGroupInputSmall",
                'placeholder': 'Обложка'
            })
        }

# ------------------------------------
