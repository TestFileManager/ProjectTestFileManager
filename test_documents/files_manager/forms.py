# --- для выгрузки файлов ---------------
from django import forms
from .models import Post
from django.forms import FileInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["comment", "upload"]
        widgets = {
            "upload":FileInput(attrs={
                "id": "img",
                "class": "display_none"
            })
        }
# ------------------------------------
