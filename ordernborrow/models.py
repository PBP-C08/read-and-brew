from django.db import models
from booklist.models import Buku
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    food_name = models.CharField(max_length=255)
    food_price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

class OrderMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=255)
    food_price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Buku, on_delete=models.CASCADE)
    borrowed = models.BooleanField(default=True)