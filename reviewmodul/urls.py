from django.urls import path
from reviewmodul.views import *

app_name = 'reviewmodul'

urlpatterns = [
    path('show_review/', show_review, name='show_review'),
    path('add_review_ajax/', add_review_ajax, name='add_review_ajax'),
    path('get-review/', get_review_json, name='get_review_json'),
    path('get-review-member/', get_review_json_member, name='get_review_json_member'),
    path('show_review/delete_review/<int:id>/', delete_review, name='delete_review'),
    path('get_borrowed_history_json_member', get_borrowed_history_json_member, name='get_borrowed_history_json_member'),
    path('json/', show_json, name='show_json'),
    path('json_jumlah_review/', show_json_jumlah_review, name='show_json_jumlah_review'),
    path('add-review-flutter/',add_review_flutter, name='add_review_flutter'),
    path('delete-review-flutter/<int:id>/', delete_review_flutter, name='delete_review_flutter'),
]