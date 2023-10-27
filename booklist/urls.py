from django.urls import path
from booklist.views import get_books, show_booklist, add_book_ajax, delete_book_ajax
app_name = 'booklist'

urlpatterns = [
    path("api/buku/", get_books, name="get_books"),
    path("", show_booklist, name="show_booklist"),
    path("add-book-ajax/", add_book_ajax, name="add_book_ajax"),
    path("delete-book-ajax/", delete_book_ajax, name="delete_book_ajax"),
]