from django.urls import path
from main.views import *
from ordernborrow.views import *


app_name = 'main'


urlpatterns = [
    path('', show_main, name='show_main'),
    path('signup/', signup, name='signup'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
]