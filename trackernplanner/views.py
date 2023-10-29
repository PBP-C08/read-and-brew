#pylint: disable=E1101
from django.shortcuts import get_object_or_404, render, redirect
from trackernplanner.models import *
from booklist.models import Buku
from ordernborrow.models import BorrowedBook
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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
    data = BookTrackerMember.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_tracker(request):
    data = BookTracker.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_borrowedbooks(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', borrowed_books))

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
    
def update_progress(request, book_id):
    if request.method == "POST":
        new_progress = request.POST.get("progress")
        book = BookTrackerMember.objects.get(pk=book_id)
        book.progress = new_progress

        if book.progress == book.page:
            book.status = 'finished'
            
        book.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()