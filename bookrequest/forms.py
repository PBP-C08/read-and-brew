from django.forms import ModelForm
from bookrequest.models import Buku

class BukuForm(ModelForm):
    class Meta:
        model = Buku
        fields = ["Gambar","Judul","Penulis","Kategori"]