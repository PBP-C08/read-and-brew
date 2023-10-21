from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from booklist.models import Buku
# Create your views here.

def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")
