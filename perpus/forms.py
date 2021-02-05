from django.forms import ModelForm
from django import forms
from .models import Buku


class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = "__all__"
        # untuk menampilkan sebagian form fields = ['judul','penulis']
        # menampilkan kecuali form ini exclude=['']

        widgets = {
            "judul": forms.TextInput({"class": "form-control"}),
            "penulis": forms.TextInput({"class": "form-control"}),
            "penerbit": forms.TextInput({"class": "form-control"}),
            "jumlah": forms.NumberInput({"class": "form-control"}),
            "kelompok_id": forms.Select({"class": "form-control"}),
        }
