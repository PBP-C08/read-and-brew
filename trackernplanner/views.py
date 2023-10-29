#pylint: disable=E1101
from django.shortcuts import render, redirect
from trackernplanner.models import *
from booklist.models import Buku
from ordernborrow.models import BorrowedBook
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers

def show_tracker_planner(request):
    is_member = False
    books_read, latest_planner = 0, None

    if request.user.is_authenticated:
        user = request.user
        is_member = True
        books_read = BookTrackerMember.objects.filter(user=user).count()
        latest_planner = BookPlanner.objects.filter(user=user).order_by('-id').first()
    else:
        guest_id = request.session.get('guest_id', None)

        if guest_id is not None:
            books_read = BookTracker.objects.filter(guest_id=guest_id).count()
            latest_planner = None

    context = {
        'is_member': is_member,
        'books_read': books_read,
        'latest_planner': latest_planner,
    }
    return render(request, 'trackernplanner.html', context)

def show_tracker_guest(request):
    return

@login_required
def show_tracker(request):
    if request.method == 'POST':
        user = request.user
        book_id = request.POST['book']
        page = request.POST['page']
        progress = request.POST['progress']
        status = request.POST['status']

        # Check if a tracker record already exists for this book and user
        tracker, created = BookTrackerMember.objects.get_or_create(
            user=user,
            book_id=book_id,
            defaults={'page': page, 'progress': progress, 'status': status}
        )

        if not created:
            # If the record already exists, update its data
            tracker.page = page
            tracker.progress = progress
            tracker.status = status
            tracker.save()

        # After handling the POST request, you should return an appropriate response
        return JsonResponse({'message': 'Book tracking updated successfully'})

    # Handle other cases, e.g., rendering a template
    return render(request, 'booktracker.html')

@login_required
def show_planner(request):
    return

def show_json(request):
    data = BookTrackerMember.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_borrowedbooks(request):
    # Retrieve the borrowed books
    borrowed_books = BorrowedBook.objects.filter(borrowed=True)
    
    # Prepare the data as JSON
    books_data = [
        {
            'pk': book.book.pk,
            'fields': {
                'Gambar': book.book.Gambar,
                'Judul': book.book.Judul,
                'Penulis': book.book.Penulis,
                'Kategori': book.book.Kategori,
                'Rating': book.book.Rating,
            }
        }
        for book in borrowed_books
    ]
    
    return JsonResponse(books_data, safe=False)