from django.urls import path
from main.views import show_main, login_user, signup, logout_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('signup/', signup, name='signup'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]