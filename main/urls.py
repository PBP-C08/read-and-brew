from django.urls import path
from main.views import show_main, login_user, signup, logout_user, food_view,drinks_view, order_food_ajax, show_order_guest, get_product_json, delete_order_ajax, edit_order_ajax,show_json,show_json_by_id, delete_allorder_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('signup/', signup, name='signup'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('order-borrow/food', food_view, name='food_menu'),
    path('order-borrow/drinks', drinks_view, name='drinks_menu'),
    path('order-food/', order_food_ajax, name='order_food_ajax'),
    path('show-order-guest/', show_order_guest, name="show_order_guest"),
    path('get-product/', get_product_json, name='get_product_json'),
    path('delete-order-ajax/<int:id>/', delete_order_ajax, name='delete_order_ajax'),
    path('delete-allorder-ajax/', delete_allorder_ajax, name='delete_allorder_ajax'),
    path('edit-order-ajax/<int:id>/', edit_order_ajax, name='edit_order_ajax'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('json/', show_json, name='show_json'),
]