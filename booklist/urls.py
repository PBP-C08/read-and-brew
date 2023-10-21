from django.urls import path
from booklist.views import get_books
app_name = 'booklist'

urlpatterns = [
    path("api/buku/", get_books, name="get_books")
]