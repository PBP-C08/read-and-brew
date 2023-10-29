from django.db import models
from django.contrib.auth.models import User

class RequestBuku(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Gambar = models.CharField(max_length=255)
    Judul = models.CharField(max_length=255)
    Penulis = models.CharField(max_length=255)
    Kategori = models.CharField(max_length=255)
    Like = models.IntegerField(default=0)
    Status = models.CharField(max_length=255, default="Waiting For Approval")