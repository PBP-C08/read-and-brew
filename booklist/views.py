import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from booklist.models import Buku
from main.models import Profile
from booklist.forms import BookForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def show_booklist(request):
    form = BookForm(request.POST or None)
    books = Buku.objects.all()
    categories = Buku.objects.values('Kategori').distinct().values_list('Kategori', flat=True)
    if request.user.is_authenticated:
        profile  = Profile.objects.filter(user=request.user).first()
        context = {
            'books': books,
            'categories': categories,
            'profile': profile,
            'form': form,
        }
    else:
        context = {
            'books': books,
            'categories': categories,
        }
    return render(request, 'booklist.html', context)
def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        Judul = request.POST.get("judul")
        Gambar = request.POST.get("gambar")
        Penulis = request.POST.get("penulis")
        Kategori = request.POST.get("kategori")

        new_book = Buku(Judul=Judul, Gambar=Gambar, Penulis=Penulis, Kategori=Kategori, Rating=0)
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_book_ajax(request):
    if request.method == "POST":
        book_id = request.POST.get("id")
        Buku.objects.filter(pk=book_id).delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def create_book_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_book = Buku.objects.create(
            Judul = data['judul'],
            Gambar = data['gambar'],
            Penulis = data['penulis'],
            Kategori = data['kategori'],
            Rating = 0
        )
        new_book.save()

        return JsonResponse({"status": "success", "messages":"Berhasil menambahkan item!"}, status=200)
    else:
        return JsonResponse({"status": "error", "messages":"Gagal menambahkan item!"}, status=401)
    
@csrf_exempt
def delete_book_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Buku.objects.filter(pk=int(data['id'])).delete()
        return JsonResponse({"status": "success", "messages":"Berhasil menghapus item!"}, status=200)
    else:
        return JsonResponse({"status": "error", "messages":"Gagal menghapus item!"}, status=401)