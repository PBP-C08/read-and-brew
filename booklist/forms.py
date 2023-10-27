from django import forms
from booklist.models import Buku

class BookForm(forms.Form):
    class meta:
        model = Buku
    judul = forms.CharField(label='Judul', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'judul'}))
    gambar = forms.CharField(label='Link Gambar', max_length=200 ,widget=forms.TextInput(attrs={'class': 'form-control', 'name':'gambar'}))
    penulis = forms.CharField(label='Penulis', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'penulis'}))
    kategori = forms.CharField(label='Kategori', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'kategori', 'list':'kategorilist'}))