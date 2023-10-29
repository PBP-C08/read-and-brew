from django.urls import path
from trackernplanner.views import *

app_name = 'trackernplanner'

urlpatterns = [
    path('', show_tracker_planner, name='show_tracker_planner'),

    path('guest/book-tracker', show_tracker_guest, name='show_tracker_guest'),

    path('member/book-tracker', show_tracker, name='show_tracker'),
    path('member/book-planner', show_planner, name='show_planner'),

    path('member/json/', show_json, name='show_json'),

    path('member/show-json-borrowedbooks/', show_json_borrowedbooks, name='show_json_borrowedbooks'),
]