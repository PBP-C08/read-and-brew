from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ReviewMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    book_name = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(default=0)
    review = models.TextField()