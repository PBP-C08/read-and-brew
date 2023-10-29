from django import forms
from booklist.models import Buku

class BookForm(forms.Form):
    class meta:
        model = Buku
    judul = forms.CharField(label='Judul', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'judul', 'placeholder':'Judul Buku', 'style':"border: 1px solid #513C1E;color: #513C1E;background-color: #FDFCF8;"}))
    gambar = forms.CharField(label='Link Gambar', max_length=200 ,widget=forms.TextInput(attrs={'class': 'form-control', 'name':'gambar', 'placeholder':'Link Gambar', 'style':"border: 1px solid #513C1E;color: #513C1E;background-color: #FDFCF8;"}))
    penulis = forms.CharField(label='Penulis', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'penulis', 'placeholder':'Penulis', 'style':"border: 1px solid #513C1E;color: #513C1E;background-color: #FDFCF8;"}))
    kategori = forms.CharField(label='Kategori', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'name':'kategori', 'list':'kategorilist', 'placeholder':'Kategori', 'style':"border: 1px solid #513C1E;color: #513C1E;background-color: #FDFCF8;"}))