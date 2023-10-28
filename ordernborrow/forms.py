from django.forms import ModelForm
from ordernborrow.models import *
from django import forms

class OrderForm(forms.Form):
    class Meta:
        model = Order
    amount = forms.IntegerField(label="Amount", widget=forms.TextInput(attrs={"class":"form-control","id":"amount", "name":"amount", "min":"1", "type":"number"}))

class OrderMemberForm(ModelForm):
    class Meta:
        model = OrderMember
        fields = ["food_name", "food_price", "amount"]


class BorrowBookForm(ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ["user", "book", "borrowed"]