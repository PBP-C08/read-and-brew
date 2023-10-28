#pylint: disable=E1101
from django.shortcuts import render, redirect
from trackernplanner.models import *
from booklist.models import Buku
from ordernborrow.models import BorrowedBook
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
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
        book_id = request.POST['book']
        page = request.POST['page']
        progress = request.POST['progress']
        
        user = request.user
        book = BorrowedBook.objects.get(pk=book_id)
        status = 'in_progress' if page != progress else 'finished'
        new_tracker = BookTrackerMember(user=user, book=book, page=page, progress=progress, status=status)
        new_tracker.save()

        return redirect('trackernplanner:show_tracker')
    
    books = BorrowedBook.objects.all()
    
    context = {
        'books': books,
    }
    return render(request, 'booktracker.html', context)

@login_required
def show_planner(request):
    return

def show_json(request):
    data = BookTrackerMember.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")