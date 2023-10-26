from django.forms import ModelForm
from ordernborrow.models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["food_name", "food_price", "amount"]

class OrderMemberForm(ModelForm):
    class Meta:
        model = OrderMember
        fields = ["food_name", "food_price", "amount"]


class BorrowBookForm(ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ["user", "book", "borrowed"]