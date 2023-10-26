from django.forms import ModelForm
from reviewmodul.models import *

class OrderMemberForm(ModelForm):
    class Meta:
        model = ReviewMember
        fields = ["username", "book_name", "rating", "review"]