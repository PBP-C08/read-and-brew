from django.shortcuts import render
from reviewmodul.models import ReviewMember
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.
def show_review(request):
    content = {
        "list_review": {
            "Zhongli":{
                'book_name': "Hand Job: A Catalog of Type",
                'rating': 4,
                'review': "Lorem ipsum bla bla bla. Lorem ipsum bla bla bla. Lorem ipsum bla bla bla."
            },
            "Jean":{
                'book_name': "Jacob A. Riis: Revealing New York's Other Half: A Complete Catalogue of His Photographs",
                'rating': 5,
                'review': "Lorem ipsum bla bla bla. Lorem ipsum bla bla bla. Lorem ipsum bla bla bla."
            },
            "Wriothesley":{
                'book_name': "Dynamic Wrinkles and Drapery: Solutions for Drawing the Clothed Figure",
                'rating': 3,
                'review': "Lorem ipsum bla bla bla. Lorem ipsum bla bla bla. Lorem ipsum bla bla bla."
            },
            "Chlorinde":{
                'book_name': "Baryshnikov: In Black and White",
                'rating': 3,
                'review': "Lorem ipsum bla bla bla. Lorem ipsum bla bla bla. Lorem ipsum bla bla bla."
            },
            "Navia":{
                'book_name': "The Bundy Murders: A Comprehensive History",
                'rating': 5,
                'review': "Lorem ipsum bla bla bla. Lorem ipsum bla bla bla. Lorem ipsum bla bla bla."
            },
            "Neuvillette":{
                'book_name': "Kiss, Bow, Or Shake Hands: The Bestselling Guide to Doing Business in More Than 60 Countries",
                'rating': 4,
                'review': "Lorem ipsum bla bla bla. Lorem ipsum bla bla bla. Lorem ipsum bla bla bla."
            }
        },
    }
    return render(request, "reviewmodul.html", content)

@login_required(login_url='/login/')
def show_review_member(request):
    review = ReviewMember.objects.filter(user=request.user)

    content = {
        'username': request.user.username,
        'myreview': review,
    }

    return render(request, "reviewmodul.html", content)

def get_review_json(request):
    review_item = ReviewMember.objects.all()
    return HttpResponse(serializers.serialize('json', review_item))

def get_review_json_member(request):
    review_item = ReviewMember.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', review_item))

@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        book_name = request.POST.get("book_name")
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        user = request.user

        new_review = ReviewMember(username=username, book_name = book_name, rating=rating, review=review, user=user)
        if int(rating)>0 and int(rating) <= 5:
            new_review.save()
            return HttpResponse(b"CREATED", status=201)
        else:
            messages.error(request, "Invalid Rating!")

    return HttpResponseNotFound()

@csrf_exempt
def delete_review(request, id):
    if request.method == "DELETE":
        my_review = ReviewMember.objects.get(pk=id)
        my_review.delete()
        return HttpResponse(b"DELETED", status=200)

    return HttpResponseNotFound()