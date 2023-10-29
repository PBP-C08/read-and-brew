from django.urls import path
from bookrequest.views import get_books, add_books, show_request, approve_request, get_books_individual, delete_request_ajax_individual, like_request_ajax, delete_request_ajax
app_name = 'bookrequest'

urlpatterns = [
    path('like_request_ajax', like_request_ajax, name='like_request_ajax'),
    path('approve_request', approve_request, name='approve_request'),
    path("", show_request, name="show_request"),
    path("get_books_individual", get_books_individual, name="get_books_individual"),
    path("get_books", get_books, name="get_books"),
    path("add_books", add_books, name="add_books"),
    path('delete-request-ajax-individual/<int:id>/', delete_request_ajax_individual, name='delete_request_ajax_individual'),
    path('delete-request-ajax', delete_request_ajax, name='delete_request_ajax'),
]