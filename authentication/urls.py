from django.urls import path
from authentication.views import login, logout, create_user_flutter

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('create-user-flutter/', create_user_flutter, name='create_user_flutter'),
]