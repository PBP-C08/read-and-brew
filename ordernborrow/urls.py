from django.urls import path
from ordernborrow.views import *

app_name = 'ordernborrow'

urlpatterns = [
    path('guest/food/', food_view, name='food_menu'),
    path('guest/drinks/', drinks_view, name='drinks_menu'),
    path('guest/order/', order_food_ajax, name='order_food_ajax'),
    path('guest/show-order/', show_order_guest, name="show_order_guest"),
    path('guest/get-product/', get_product_json, name='get_product_json'),
    path('guest/delete-order-ajax/<int:id>/', delete_order_ajax, name='delete_order_ajax'),
    path('guest/delete-allorder-ajax/', delete_allorder_ajax, name='delete_allorder_ajax'),
    path('guest/edit-order-ajax/<int:id>/', edit_order_ajax, name='edit_order_ajax'),
    path('guest/json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('guest/json/', show_json, name='show_json'),
    path('member/food', food_view_member, name='food_menu_member'),
    path('member/drinks', drinks_view_member, name='drinks_menu_member'),
    path('member/order/', order_food_ajax_member, name='order_food_ajax_member'),
    path('member/secretmenu', secret_menu_view, name='secret_menu_view'),
    path('member/show-order/', show_order_member, name="show_order_member"),
    path('member/get-product/', get_product_json_member, name='get_product_json_member'),
    path('member/delete-order-ajax/<int:id>/', delete_order_ajax_member, name='delete_order_ajax_member'),
    path('member/delete-allorder-ajax/', delete_allorder_ajax_member, name='delete_allorder_ajax_member'),
    path('member/edit-order-ajax/<int:id>/', edit_order_ajax_member, name='edit_order_ajax_member'),
    path('member/json/<int:id>/', show_json_by_id_member, name='show_json_by_id_member'),
    path('member/json/', show_json_member, name='show_json_member'),
    
]