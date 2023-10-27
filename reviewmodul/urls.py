from django.urls import path
from reviewmodul.views import *

app_name = 'reviewmodul'

urlpatterns = [
    path('show_review/', show_review, name='show_review'),
    path('add_review_ajax/', add_review_ajax, name='add_review_ajax'),
    path('get-review/', get_review_json, name='get_review_json'),
    path('get-review-member/', get_review_json_member, name='get_review_json_member'),
    path('show_review_member/', show_review_member, name='show_review_member'),
    path('show_review/delete_review/<int:id>/', delete_review, name='delete_review')
]