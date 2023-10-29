from django.urls import path
from trackernplanner.views import *

app_name = 'trackernplanner'

urlpatterns = [
    path('', show_tracker_planner, name='show_tracker_planner'),

    path('book-tracker-guest', show_tracker_guest, name='show_tracker_guest'),

    path('book-tracker', show_tracker, name='show_tracker'),
    path('book-planner', show_planner, name='show_planner'),
    path('show-json-borrowedbooks', show_json_borrowedbooks, name='show_json_borrowedbooks'),
    path('track-book', track_book, name='track_book'),

    path('show-json-trackermember', show_json_trackermember, name='show_json_trackermember'),
    path('get-book-details', get_book_details, name='get_book_details'),
    path('update-progress/<int:book_id>', update_progress, name='update_progress'),
]