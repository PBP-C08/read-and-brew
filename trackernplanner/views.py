#pylint: disable=E1101
import json
from django.shortcuts import get_object_or_404, render, redirect
from trackernplanner.models import *
from booklist.models import Buku
from ordernborrow.models import BorrowedBook
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

def show_tracker_planner(request):
    is_member = False
    books_read = 0

    if request.user.is_authenticated:
        user = request.user
        is_member = True
        books_read = BookTrackerMember.objects.filter(user=user).count()
    else:
        guest_id = request.session.get('guest_id', None)

        if guest_id is not None:
            books_read = BookTracker.objects.filter(guest_id=guest_id).count()

    context = {
        'is_member': is_member,
        'books_read': books_read,
    }
    return render(request, 'trackernplanner.html', context)

@csrf_exempt
def track_book(request):
    if request.method == "POST":
        user = request.user
        book_id = request.POST.get("book")
        page = request.POST.get("page")
        progress = request.POST.get("progress")
        status = request.POST.get("status")

        #get the instance of the book
        book = get_object_or_404(Buku, pk=book_id)

        new_booktrack = BookTrackerMember(
            user=user,
            book=book,
            page=page,
            progress=progress,
            status=status
        )
        new_booktrack.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def track_book_guest(request):
    if request.method == "POST":
        book_id = request.POST.get("book")
        page = request.POST.get("page")
        progress = request.POST.get("progress")
        status = request.POST.get("status")

        #get the instance of the book
        book = get_object_or_404(Buku, pk=book_id)

        new_booktrack = BookTracker(
            book=book,
            page=page,
            progress=progress,
            status=status
        )
        new_booktrack.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def show_json_trackermember(request):
    data = BookTrackerMember.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_trackermember_flutter(request):
    data = BookTrackerMember.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_tracker(request):
    data = BookTracker.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_borrowedbooks(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', borrowed_books))

def show_json_borrowedbooks_flutter(request):
    borrowed_books = BorrowedBook.objects.all()
    return HttpResponse(serializers.serialize("json", borrowed_books), content_type="application/json")

def get_book_details(request, book_id):
    if request.method == "GET":
        book = Buku.objects.get(id=book_id)

        book_data = {
            'Gambar': book.Gambar,
            'Judul': book.Judul,
            'Kategori': book.Kategori,
            'Penulis': book.Penulis,
            'Rating': book.Rating,
        }

        return JsonResponse(book_data)

@csrf_exempt
def update_progress(request, book_id):
    if request.method == "POST":
        new_progress = request.POST.get("progress")
        book = BookTracker.objects.get(pk=book_id)
        book.progress = new_progress

        if int(book.progress) == int(book.page):
            book.status = 'finished' 
        else:
            book.status = 'in-progress'

        book.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def update_progress_member(request, book_id):
    if request.method == "POST":
        new_progress = request.POST.get("progress")
        book = BookTrackerMember.objects.get(pk=book_id)
        book.progress = new_progress

        if int(book.progress) == int(book.page):
            book.status = 'finished' 
        else:
            book.status = 'in-progress'

        book.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def track_book_guest_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)

        book_instance = Buku.objects.get(pk=data["book"])

        new_product = BookTracker.objects.create(
            book = book_instance,
            page = int(data["page"]),
            progress = int(data["progress"]),
            status = data["status"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def track_book_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)

        book_instance = Buku.objects.get(pk=data["book"])

        new_product = BookTrackerMember.objects.create(
            user = request.user,
            book = book_instance,
            page = int(data["page"]),
            progress = int(data["progress"]),
            status = data["status"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def update_progress_flutter(request, book_id):
    if request.method == "POST":
        data = json.loads(request.body)

        new_progress = int(data["progress"])
        book = BookTracker.objects.get(book=int(book_id))
        book.progress = new_progress

        if int(book.progress) == int(book.page):
            book.status = 'finished' 
        else:
            book.status = 'in-progress'

        book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def update_progress_member_flutter(request, book_id):
    if request.method == "POST":
        data = json.loads(request.body)

        new_progress = int(data["progress"])
        book = BookTrackerMember.objects.get(book=int(book_id))
        book.progress = new_progress

        if int(book.progress) == int(book.page):
            book.status = 'finished' 
        else:
            book.status = 'in-progress'

        book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def delete_book_member(request, id):
    if request.method == 'DELETE':
        item = BookTrackerMember.objects.get(pk=id)
        item.delete()
        return HttpResponse()
    return HttpResponseNotFound()

@csrf_exempt
def delete_book_member_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        book_id = int(data["id"])
        item = BookTrackerMember.objects.get(book=int(book_id))
        item.delete()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def delete_old_books(request):
    if request.method == 'POST':
        time_threshold = timezone.now() - timezone.timedelta(hours=48)
        old_books = BookTracker.objects.filter(tracked_at__lt=time_threshold)
        count = old_books.count()
        old_books.delete()

        return JsonResponse({"status": "success", "count": count}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)