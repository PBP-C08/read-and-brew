from django.urls import path
from ordernborrow.views import *

app_name = 'ordernborrow'

urlpatterns = [
    path('guest/food/', food_view, name='food_menu'),
    path('guest/drinks/', drinks_view, name='drinks_menu'),
    path('guest/order/', order_food_ajax, name='order_food_ajax'),
    path('guest/order-summary/', show_order_guest, name="show_order_guest"),
    path('guest/get-product/', get_product_json, name='get_product_json'),
    path('guest/delete-order-ajax/<int:id>/', delete_order_ajax, name='delete_order_ajax'),
    path('guest/delete-all-order-ajax/', delete_allorder_ajax, name='delete_allorder_ajax'),
    path('guest/edit-order-ajax/<int:id>/', edit_order_ajax, name='edit_order_ajax'),

    path('member/food', food_view_member, name='food_menu_member'),
    path('member/drinks', drinks_view_member, name='drinks_menu_member'),
    path('member/order/', order_food_ajax_member, name='order_food_ajax_member'),
    path('member/secret-menu', secret_menu_view, name='secret_menu_view'),
    path('member/order-summary/', show_order_member, name="show_order_member"),
    path('member/get-product/', get_product_json_member, name='get_product_json_member'),
    path('member/delete-order-ajax/<int:id>/', delete_order_ajax_member, name='delete_order_ajax_member'),
    path('member/delete-all-order-ajax/', delete_allorder_ajax_member, name='delete_allorder_ajax_member'),
    path('member/edit-order-ajax/<int:id>/', edit_order_ajax_member, name='edit_order_ajax_member'),

    path('member/borrow/', show_books, name='show_books'),
    path('member/show-borrowed/', show_borrowed_books, name='show_borrowed_books'),
    path('member/borrow-book/', borrow_book_member, name='borrow_book_member'),
    path('member/return-book/<int:id>/', return_book_member, name='return_book_member'),
    path('member/borrowed/', show_json_borrowedbooks, name='show_json_borrowedbooks'),
    path('member/borrowed-history/', show_json_borrowedhistory, name='show_json_borrowedhistory'),
    path('member/show-borrowed-history/', show_borrowed_history, name='show_borrowed_history'),
    path('member/create-borrowed-history/', create_borrowed_history, name='create_borrowed_history'),

    path('employee/supplies-equipment/', supplies_and_equipment_view, name='supplies_and_equipment_view'),

    path('guest/api/get-food/', get_food, name="get_food"),
    path('guest/api/get-drink/', get_drink, name="get_drink"),
    path('guest/order-drink-flutter/', create_order_flutter, name="order_drink"),
    path('guest/order-food-flutter/', create_order_flutter, name="order_food"),
    path('guest/delete-all-order-flutter/', delete_allorder_flutter, name='delete_allorder_flutter'),
    path('guest/edit-order-flutter/<int:id>/', edit_order_flutter, name='edit_order_flutter'),
    path('guest/delete-order-flutter/<int:id>/', delete_order_flutter, name='delete_order_flutter'),
]