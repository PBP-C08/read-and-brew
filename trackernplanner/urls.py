from django.urls import path
from trackernplanner.views import *

app_name = 'trackernplanner'

urlpatterns = [
    path('', show_tracker_planner, name='show_tracker_planner'),
    path('show-json-borrowedbooks', show_json_borrowedbooks, name='show_json_borrowedbooks'),
    path('track-book', track_book, name='track_book'),
    path('track-book-guest', track_book_guest, name='track_book_guest'),
    path('show-json-trackermember', show_json_trackermember, name='show_json_trackermember'),
    path('show-json-tracker', show_json_tracker, name='show_json_tracker'),
    path('get-book-details', get_book_details, name='get_book_details'),
    path('update-progress/<int:book_id>', update_progress, name='update_progress'),
]