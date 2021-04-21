# --- для выгрузки файлов ---------------
from django import forms
from .models import Book
from django.forms import FileInput
# -----------Форма с книгами----------


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name', 'short_description', 'description',
            'cover', 'file', 'author'
                 ]
        widgets = {
            'file': FileInput(attrs={
                "id": "img",
                "class": "display_none"
            }),
            'cover': FileInput(attrs={
                "id": "img",
                "class": "display_none"
            })
        }

# ------------------------------------
