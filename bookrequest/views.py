import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bookrequest.models import RequestBuku
from django.core import serializers
from django.contrib.auth.decorators import login_required
from booklist.models import Buku

# Create your views here.
@login_required(login_url='/login')
def show_request(request):
    buku = RequestBuku.objects.all()

    context = {
        'buku':buku
    }

    return render(request, "bookrequest.html", context)

def get_books_individual(request):
    buku = RequestBuku.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', buku), content_type="application/json")

def get_books(request):
    data = RequestBuku.objects.all()
    print(data)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

@csrf_exempt
def add_books(request):
    if request.method == 'POST':
        user = request.user
        Gambar = request.POST.get("Gambar")
        Judul = request.POST.get("Judul")
        Penulis = request.POST.get("Penulis")
        Kategori = request.POST.get("Kategori")

        new_product = RequestBuku(user=user, Gambar=Gambar, Judul=Judul, Penulis=Penulis, Kategori=Kategori, Like=0)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
@login_required(login_url='/login')
def unlike_book(request, id):
    if request.method == 'POST':
        buku = get_object_or_404(RequestBuku, pk=id)

        # Check if the user has liked the book to prevent unliking if not liked
        if buku.likes.filter(id=request.user.id).exists():
            buku.Like -= 1
            buku.likes.remove(request.user)
            buku.save()
            return JsonResponse({'likes': buku.Like, 'liked': False})
        else:
            return JsonResponse({'error': 'You cannot unlike this book.', 'liked': True}, status=400)

    return HttpResponseNotFound()

@csrf_exempt
def approve_request(request):
    if request.method == "POST":
        book_id = request.POST.get("id")
        request_buku = RequestBuku.objects.get(pk=book_id)
        request_buku.Status = "Approved"
        request_buku.save()
        judul = request_buku.Judul
        kategori = request_buku.Kategori
        gambar = request_buku.Gambar
        penulis = request_buku.Penulis
        buku = Buku(Judul=judul, Kategori=kategori, Gambar=gambar, Penulis=penulis, Rating=0)
        buku.save()
        return HttpResponse(b"APPROVED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def delete_request_ajax(request):
    if request.method == "POST":
        book_id = request.POST.get("id")
        RequestBuku.objects.filter(pk=book_id).delete()
        return HttpResponse(b"DELETED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def delete_request_ajax_individual(request, id):
    if request.method == 'DELETE':
        item = RequestBuku.objects.get(pk=id, user=request.user)
        item.delete()
        return HttpResponse(b"DELETED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def like_request_ajax(request):
    if request.method == "POST":
        book_id = request.POST.get("id")
        book = RequestBuku.objects.get(pk=book_id)
        book.Like += 1
        book.save()
        return HttpResponse(b"LIKED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def create_request_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_request = RequestBuku.objects.create(
            user = request.user,
            Judul = data['judul'],
            Gambar = data['gambar'],
            Penulis = data['penulis'],
            Kategori = data['kategori'],
            Like = 0,
            Status = "Waiting For Approval"
        )
        new_request.save()

        return JsonResponse({"status": "success", "messages":"Berhasil menambahkan item!"}, status=200)
    else:
        return JsonResponse({"status": "error", "messages":"Gagal menambahkan item!"}, status=401)

@csrf_exempt
def delete_request_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        RequestBuku.objects.filter(pk=int(data['id'])).delete()
        return JsonResponse({"status": "success", "messages":"Berhasil menghapus request!"}, status=200)
    else:
        return JsonResponse({"status": "error", "messages":"Gagal menghapus request!"}, status=401)
    
@csrf_exempt
def like_request_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        book = RequestBuku.objects.filter(pk=int(data['id']))
        book.Like += 1
        return JsonResponse({"status": "success", "messages":"Berhasil menambah like!"}, status=200)
    else:
        return JsonResponse({"status": "error", "messages":"Gagal menambah like!"}, status=401)
    
@csrf_exempt
def approve_request_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        request_buku = RequestBuku.objects.filter(pk=int(data['id']))
        request_buku.Status = "Approved"
        request_buku.save()
        judul = request_buku.Judul
        kategori = request_buku.Kategori
        gambar = request_buku.Gambar
        penulis = request_buku.Penulis
        buku = Buku(Judul=judul, Kategori=kategori, Gambar=gambar, Penulis=penulis, Rating=0)
        buku.save()
        return HttpResponse(b"APPROVED", status=201)
    return HttpResponseNotFound()