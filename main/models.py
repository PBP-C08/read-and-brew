from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=1)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)

class Order(models.Model):
    food_name = models.CharField(max_length=255)
    food_price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.username} ordered {self.food_name} on {self.order_date}"

