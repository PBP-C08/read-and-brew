from django.db import models

class Buku(models.Model):
    Gambar = models.CharField(max_length=255)
    Judul = models.CharField(max_length=255)
    Penulis = models.CharField(max_length=255)
    Kategori = models.CharField(max_length=255)
    Rating = models.IntegerField()