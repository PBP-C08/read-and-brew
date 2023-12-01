#pylint: disable=E1101
import json
from django.shortcuts import render
from reviewmodul.models import ReviewMember, JumlahReview
from ordernborrow.models import BorrowedHistory
from booklist.models import Buku
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.
def show_review(request):
    return render(request, "reviewmodul.html")

def get_review_json(request):
    review_item = ReviewMember.objects.all()
    return HttpResponse(serializers.serialize('json', review_item))

def show_json(request):
    data = ReviewMember.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_jumlah_review(request):
    data = JumlahReview.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_review_json_member(request):
    review_item = ReviewMember.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', review_item))

def get_borrowed_history_json_member(request):
    history = BorrowedHistory.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', history))

@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        book_name = request.POST.get("book_name")
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        user = request.user

        new_review = ReviewMember(username=username, book_name = book_name, rating=rating, review=review, user=user)
        jumlahReview = JumlahReview.objects.filter(book__Judul=book_name).first()
        buku = Buku.objects.filter(Judul=book_name).first()
       
        if(jumlahReview == None):
            jumlahReview = JumlahReview(book=buku, jumlah = 0)
        
        jumlahReview.jumlah += 1

        if int(rating)>0 and int(rating) <= 5:
            jumlahReview.save()
            buku.Rating = int((buku.Rating + int(rating))/jumlahReview.jumlah)
            buku.save()
            new_review.save()
            
            return HttpResponse(b"CREATED", status=201)
        else:
            messages.error(request, "Invalid Rating!")
    
    return HttpResponseNotFound()

@csrf_exempt
def delete_review(request, id):
    if request.method == "DELETE":
        my_review = ReviewMember.objects.get(pk=id)
        jumlahReview = JumlahReview.objects.filter(book__Judul=my_review.book_name).first()
        buku = Buku.objects.filter(Judul=my_review.book_name).first()

        try:
            buku.Rating = int(((buku.Rating*jumlahReview.jumlah) - my_review.rating) / (jumlahReview.jumlah - 1))
        except ZeroDivisionError:
            buku.Rating = 0
       
        jumlahReview.jumlah -= 1
        
        jumlahReview.save()
        buku.save()
        my_review.delete()

        return HttpResponse(b"DELETED", status=200)

    return HttpResponseNotFound()

@csrf_exempt
def add_review_flutter(request):
    if request.method == "POST":
        input = json.loads(request.body)

        username = input['username']
        book_name = input['bookname']
        rating = input['rating']
        review = input['review']
        user = request.user

        new_review = ReviewMember(username=username, book_name = book_name, rating=rating, review=review, user=user)
        jumlahReview = JumlahReview.objects.filter(book__Judul=book_name).first()
        buku = Buku.objects.filter(Judul=book_name).first()
       
        if(jumlahReview == None):
            jumlahReview = JumlahReview(book=buku, jumlah = 0)
        
        jumlahReview.jumlah += 1

        if int(rating)>0 and int(rating) <= 5:
            jumlahReview.save()
            buku.Rating = int((buku.Rating + int(rating))/jumlahReview.jumlah)
            buku.save()
            new_review.save()
            
            return JsonResponse({
                "status": True,
                "message": "Success!"
            }, status=200)

        else:
            return JsonResponse({"status": False, "message": "Invalid Rating!"}, status=400)
    
    return JsonResponse({"status": False, "message": "Failed!"}, status=400)