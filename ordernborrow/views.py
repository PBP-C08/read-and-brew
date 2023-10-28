from django.shortcuts import render
from ordernborrow.models import *
from booklist.models import Buku
from ordernborrow.forms import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# For Guest (no login)
def food_view(request):
    form = OrderForm(request.POST or None)
    content = {
        "forms": form,
        "food":{
            "Bagel with Cream Cheese": {
                "price": 2.99,
                "description": "A freshly baked bagel served with a generous portion of cream cheese.",
                "ordered": Order.objects.filter(food_name="Bagel with Cream Cheese").exists()
            },
            "Egg and Cheese Sandwich": {
                "price": 4.49,
                "description": "A breakfast classic - scrambled eggs and melted cheese on a toasted bun.",
                "ordered": Order.objects.filter(food_name="Egg and Cheese Sandwich").exists()
            },
            "Cinnamon Roll": {
                "price": 3.49,
                "description": "A sweet and gooey cinnamon roll with icing on top.",
                "ordered": Order.objects.filter(food_name="Cinnamon Roll").exists()

            },
            "Chocolate Croissant": {
                "price": 2.99,
                "description": "A buttery and flaky croissant mixed with chocolate, perfect with your coffee.",
                "ordered": Order.objects.filter(food_name="Croissant").exists()

            },
            "New York Style Pizza": {
                "price": 9.99,
                "description": "A classic thin-crust pizza with your choice of toppings, just like in the Big Apple.",
                "ordered": Order.objects.filter(food_name="New York Style Pizza").exists()
            },
            "Chicago Deep Dish Pizza": {
                "price": 12.99,
                "description": "A thick and cheesy deep-dish pizza, a Windy City specialty.",
                "ordered": Order.objects.filter(food_name="Chicago Deep Dish Pizza").exists()
            },
            "Caprese Panini": {
                "price": 7.99,
                "description": "Fresh mozzarella, ripe tomatoes, and basil pesto on grilled ciabatta bread.",
                "ordered": Order.objects.filter(food_name="Caprese Panini").exists()

            },
            "Chicken Quesadilla": {
                "price": 8.49,
                "description": "Sliced chicken, cheese, and vegetables folded in a tortilla and grilled.",
                "ordered": Order.objects.filter(food_name="Chicken Quesadilla").exists()
            },
            "Spinach and Feta Quiche": {
                "price": 6.99,
                "description": "A savory pastry filled with spinach, feta cheese, and eggs.",
                "ordered": Order.objects.filter(food_name="Spinach and Feta Quiche").exists()
            },
            "Avocado Toast": {
                "price": 5.99,
                "description": "Sliced avocado on toasted artisan bread, topped with seasoning.",
                "ordered": Order.objects.filter(food_name="Avocado Toast").exists()
            },
            "Muffin": {
                "price": 2.49,
                "description": "A freshly baked muffin in your choice of flavor.",
                "ordered": Order.objects.filter(food_name="Muffin").exists()
            },
            "Blueberry Scone": {
                "price": 2.79,
                "description": "A tender and crumbly scone filled with juicy blueberries.",
                "ordered": Order.objects.filter(food_name="Blueberry Scone").exists()

            },
            "Breakfast Burrito": {
                "price": 6.49,
                "description": "A hearty breakfast burrito filled with eggs, sausage, cheese, and vegetables.",
                "ordered": Order.objects.filter(food_name="Breakfast Burrito").exists()
            },
            "Fruit Parfait": {
                "price": 4.99,
                "description": "A delicious parfait made with yogurt, granola, and a mix of fresh fruits.",
                "ordered": Order.objects.filter(food_name="Fruit Parfait").exists()
            },
            "Quiche Lorraine": {
                "price": 6.99,
                "description": "A classic quiche filled with bacon, Swiss cheese, and a savory custard.",
                "ordered": Order.objects.filter(food_name="Quiche Lorraine").exists()
            }
        }
    }

    return render(request, 'foodmenu.html', content)

# For Member (login)
def food_view_member(request):
    content = {
        "food":{
            "Bagel with Cream Cheese": {
                "price": 2.99,
                "description": "A freshly baked bagel served with a generous portion of cream cheese.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Bagel with Cream Cheese").exists()
            },
            "Egg and Cheese Sandwich": {
                "price": 4.49,
                "description": "A breakfast classic - scrambled eggs and melted cheese on a toasted bun.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Egg and Cheese Sandwich").exists()
            },
            "Cinnamon Roll": {
                "price": 3.49,
                "description": "A sweet and gooey cinnamon roll with icing on top.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Cinnamon Roll").exists()

            },
            "Chocolate Croissant": {
                "price": 2.99,
                "description": "A buttery and flaky croissant mixed with chocolate, perfect with your coffee.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Croissant").exists()

            },
            "New York Style Pizza": {
                "price": 9.99,
                "description": "A classic thin-crust pizza with your choice of toppings, just like in the Big Apple.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="New York Style Pizza").exists()
            },
            "Chicago Deep Dish Pizza": {
                "price": 12.99,
                "description": "A thick and cheesy deep-dish pizza, a Windy City specialty.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Chicago Deep Dish Pizza").exists()
            },
            "Caprese Panini": {
                "price": 7.99,
                "description": "Fresh mozzarella, ripe tomatoes, and basil pesto on grilled ciabatta bread.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Caprese Panini").exists()

            },
            "Chicken Quesadilla": {
                "price": 8.49,
                "description": "Sliced chicken, cheese, and vegetables folded in a tortilla and grilled.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Chicken Quesadilla").exists()
            },
            "Spinach and Feta Quiche": {
                "price": 6.99,
                "description": "A savory pastry filled with spinach, feta cheese, and eggs.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Spinach and Feta Quiche").exists()
            },
            "Avocado Toast": {
                "price": 5.99,
                "description": "Sliced avocado on toasted artisan bread, topped with seasoning.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Avocado Toast").exists()
            },
            "Muffin": {
                "price": 2.49,
                "description": "A freshly baked muffin in your choice of flavor.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Muffin").exists()
            },
            "Blueberry Scone": {
                "price": 2.79,
                "description": "A tender and crumbly scone filled with juicy blueberries.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Blueberry Scone").exists()

            },
            "Breakfast Burrito": {
                "price": 6.49,
                "description": "A hearty breakfast burrito filled with eggs, sausage, cheese, and vegetables.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Breakfast Burrito").exists()
            },
            "Fruit Parfait": {
                "price": 4.99,
                "description": "A delicious parfait made with yogurt, granola, and a mix of fresh fruits.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Fruit Parfait").exists()
            },
            "Quiche Lorraine": {
                "price": 6.99,
                "description": "A classic quiche filled with bacon, Swiss cheese, and a savory custard.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Quiche Lorraine").exists()
            }
        }
    }

    return render(request, 'foodmenumember.html', content)

# For Guest (no login)
def drinks_view(request):
    content = {
        "drinks": {
            "Latte": {
                "price": 3.99,
                "description": "Espresso with creamy steamed milk and a hint of vanilla.",
                "ordered": Order.objects.filter(food_name="Latte").exists()
            },
            "Cappuccino": {
                "price": 4.49,
                "description": "Espresso topped with frothy milk and a sprinkle of cocoa.",
                "ordered": Order.objects.filter(food_name="Cappuccino").exists()
            },
            "Mocha": {
                "price": 4.99,
                "description": "Rich espresso with velvety steamed milk, cocoa, and whipped cream.",
                "ordered": Order.objects.filter(food_name="Mocha").exists()
            },
            "Iced Coffee": {
                "price": 3.49,
                "description": "Chilled coffee brewed to perfection, served with ice cubes.",
                "ordered": Order.objects.filter(food_name="Iced Coffee").exists()
            },
            "Espresso": {
                "price": 2.49,
                "description": "A shot of intense, concentrated coffee to awaken your senses.",
                "ordered": Order.objects.filter(food_name="Espresso").exists()
            },
            "Chai Latte": {
                "price": 4.99,
                "description": "Spiced black tea combined with frothy milk for a delightful balance.",
                "ordered": Order.objects.filter(food_name="Chai Latte").exists()
            },
            "Caramel Macchiato": {
                "price": 4.99,
                "description": "Espresso with steamed milk, caramel, and a caramel drizzle.",
                "ordered": Order.objects.filter(food_name="Caramel Macchiato").exists()
            },
            "Iced Tea": {
                "price": 3.29,
                "description": "Chilled tea infused with fruit essence, served over ice.",
                "ordered": Order.objects.filter(food_name="Iced Tea").exists()
            },
            "Hot Chocolate": {
                "price": 3.99,
                "description": "Silky hot cocoa topped with whipped cream and chocolate shavings.",
                "ordered": Order.objects.filter(food_name="Hot Chocolate").exists()
            },
            "Fruit Smoothie": {
                "price": 4.49,
                "description": "A refreshing blend of fresh fruits, yogurt, and ice.",
                "ordered": Order.objects.filter(food_name="Fruit Smoothie").exists()
            },
            "Café Americano": {
                "price": 2.99,
                "description": "Espresso with hot water, delivering a bold and robust flavor.",
                "ordered": Order.objects.filter(food_name="Café Americano").exists()
            },
            "Matcha Latte": {
                "price": 4.99,
                "description": "Green tea powder mixed with creamy steamed milk, for a vibrant experience.",
                "ordered": Order.objects.filter(food_name="Matcha Latte").exists()
            },
            "Iced Latte": {
                "price": 4.29,
                "description": "Chilled espresso and milk served over ice, the perfect cool-down.",
                "ordered": Order.objects.filter(food_name="Iced Latte").exists()
            },
            "White Chocolate Mocha": {
                "price": 4.99,
                "description": "Espresso with white chocolate and whipped cream, pure indulgence.",
                "ordered": Order.objects.filter(food_name="White Chocolate Mocha").exists()
            },
            "Decaf Coffee": {
                "price": 3.49,
                "description": "A soothing cup of coffee with minimal caffeine content.",
                "ordered": Order.objects.filter(food_name="Decaf Coffee").exists()
            }
        }
    }

    return render(request, 'drinkmenu.html', content)

# For Member (login)
def drinks_view_member(request):
    content = {
        "drinks": {
            "Latte": {
                "price": 3.99,
                "description": "Espresso with creamy steamed milk and a hint of vanilla.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Latte").exists()
            },
            "Cappuccino": {
                "price": 4.49,
                "description": "Espresso topped with frothy milk and a sprinkle of cocoa.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Cappuccino").exists()
            },
            "Mocha": {
                "price": 4.99,
                "description": "Rich espresso with velvety steamed milk, cocoa, and whipped cream.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Mocha").exists()
            },
            "Iced Coffee": {
                "price": 3.49,
                "description": "Chilled coffee brewed to perfection, served with ice cubes.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Iced Coffee").exists()
            },
            "Espresso": {
                "price": 2.49,
                "description": "A shot of intense, concentrated coffee to awaken your senses.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Espresso").exists()
            },
            "Chai Latte": {
                "price": 4.99,
                "description": "Spiced black tea combined with frothy milk for a delightful balance.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Chai Latte").exists()
            },
            "Caramel Macchiato": {
                "price": 4.99,
                "description": "Espresso with steamed milk, caramel, and a caramel drizzle.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Caramel Macchiato").exists()
            },
            "Iced Tea": {
                "price": 3.29,
                "description": "Chilled tea infused with fruit essence, served over ice.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Iced Tea").exists()
            },
            "Hot Chocolate": {
                "price": 3.99,
                "description": "Silky hot cocoa topped with whipped cream and chocolate shavings.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Hot Chocolate").exists()
            },
            "Fruit Smoothie": {
                "price": 4.49,
                "description": "A refreshing blend of fresh fruits, yogurt, and ice.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Fruit Smoothie").exists()
            },
            "Café Americano": {
                "price": 2.99,
                "description": "Espresso with hot water, delivering a bold and robust flavor.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Café Americano").exists()
            },
            "Matcha Latte": {
                "price": 4.99,
                "description": "Green tea powder mixed with creamy steamed milk, for a vibrant experience.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Matcha Latte").exists()
            },
            "Iced Latte": {
                "price": 4.29,
                "description": "Chilled espresso and milk served over ice, the perfect cool-down.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Iced Latte").exists()
            },
            "White Chocolate Mocha": {
                "price": 4.99,
                "description": "Espresso with white chocolate and whipped cream, pure indulgence.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="White Chocolate Mocha").exists()
            },
            "Decaf Coffee": {
                "price": 3.49,
                "description": "A soothing cup of coffee with minimal caffeine content.",
                "ordered": OrderMember.objects.filter(user = request.user).filter(food_name="Decaf Coffee").exists()
            }
        }
    }

    return render(request, 'drinkmenumember.html', content)

# For Member (login)
def secret_menu_view(request):
    content = {
        "secret_food": {
            "Mystery Meatball Sub": {
                "price": 5.99,
                "description": "Indulge in succulent meatballs smothered in rich marinara sauce, tucked into a warm sub roll with a surprising twist.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Mystery Meatball Sub").exists()
            },
            "Stealthy Spinach Salad": {
                "price": 6.49,
                "description": "Discover a secret blend of fresh ingredients in a vibrant spinach salad that's a hidden gem on the menu.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Stealthy Spinach Salad").exists()
            },
            "Undercover Veggie Wrap": {
                "price": 7.99,
                "description": "Embark on a culinary adventure with a veggie wrap featuring a secret sauce that adds a delightful kick.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Undercover Veggie Wrap").exists()
            },
            "Intrigue Italian Pasta": {
                "price": 8.49,
                "description": "Savor a top-secret Italian pasta dish, expertly prepared with a balance of bold and delightful flavors.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Intrigue Italian Pasta").exists()
            },
            "Hidden Hummus Platter": {
                "price": 9.99,
                "description": "Whisper the secret password and relish a hummus platter adorned with an array of concealed toppings, perfect for sharing.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Hidden Hummus Platter").exists()
            },
            "Classified Cheeseburger": {
                "price": 4.49,
                "description": "Uncover the mystery of a classic cheeseburger with an intriguing twist that will leave your taste buds guessing.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Classified Cheeseburger").exists()
            }
        },
        "secret_drinks": {
            "Covert Caramel Latte": {
                "price": 5.99,
                "description": "Experience the allure of a caramel latte, where sweetness meets velvety espresso in a delightful rendezvous.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Covert Caramel Latte").exists()
            },
            "Stealthy Strawberry Smoothie": {
                "price": 6.49,
                "description": "Delight in a secret blend of fresh strawberries and creamy yogurt, with a hint of enchantment that will whisk you away.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Stealthy Strawberry Smoothie").exists()
            },
            "Undercover Coconut Mocha": {
                "price": 7.99,
                "description": "Unearth the hidden tropical delight of a mocha, where rich coffee meets the lusciousness of coconut in an unexpected combination.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Undercover Coconut Mocha").exists()
            },
            "Espionage Espresso Con Panna": {
                "price": 8.49,
                "description": "Embark on a covert mission with an espresso that's topped with a luxurious dollop of whipped cream, an indulgent treat shrouded in secrecy.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Espionage Espresso Con Panna").exists()
            },
            "Intrigue Iced Chai": {
                "price": 9.99,
                "description": "Unlock the secret and enjoy an iced chai latte, crafted with a special blend of spices that will captivate your taste buds.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Intrigue Iced Chai").exists()
            },
            "Classified Cold Brew": {
                "price": 4.49,
                "description": "Discover the well-aged mystery of a cold brew, where time and precision create a coffee masterpiece that's aged to perfection.",
                "ordered": OrderMember.objects.filter(user=request.user).filter(food_name="Classified Cold Brew").exists()
            }
        }
    }

    return render(request, 'secretmenu.html', content)

# For Employee (login)
def supplies_and_equipment_view(request):
    content = {
        "supplies_and_equipment" : {
            "Coffee Beans": {
                "description": "Freshly roasted coffee beans for the perfect brew.",
                "amount": 50
            },
            "Espresso Machine": {
                "description": "High-quality espresso machine for your coffee needs.",
                "amount": 5
            },
            "Milk Frother": {
                "description": "Efficient milk frother to create creamy lattes and cappuccinos.",
                "amount": 10
            },
            "Coffee Cups": {
                "description": "Disposable coffee cups for takeout orders.",
                "amount": 200
            },
            "Coffee Filters": {
                "description": "Coffee filters for your drip coffee maker.",
                "amount": 1000
            },
            "Tea Bags": {
                "description": "Assorted tea bags for a variety of flavors.",
                "amount": 100
            },
            "Coffee Grinder": {
                "description": "Professional coffee grinder for fresh coffee grounds.",
                "amount": 8
            },
            "Syrup Dispenser": {
                "description": "Dispenser for flavored syrups for your beverages.",
                "amount": 15
            },
            "Coffee Stirrers": {
                "description": "Wooden coffee stirrers for stirring hot beverages.",
                "amount": 500
            },
            "Sugar Packets": {
                "description": "Individual sugar packets for sweetening drinks.",
                "amount": 300
            },
            "Hot Water Kettle": {
                "description": "Electric kettle for boiling water quickly.",
                "amount": 6
            },
            "Espresso Cups": {
                "description": "Espresso shot cups for serving espresso shots.",
                "amount": 50
            },
            "Lids for Cups": {
                "description": "Plastic lids for coffee cups to prevent spills.",
                "amount": 400
            },
            "Napkins": {
                "description": "Paper napkins for customers to use.",
                "amount": 1000
            },
            "Coffee Spoons": {
                "description": "Small coffee spoons for stirring hot drinks.",
                "amount": 600
            },
            "Coffee Creamer": {
                "description": "Dairy and non-dairy creamer options for coffee.",
                "amount": 40
            },
            "Cocoa Powder": {
                "description": "High-quality cocoa powder for making hot chocolate.",
                "amount": 20
            },
            "Disposable Stirrers": {
                "description": "Disposable stirrers for hot and cold drinks.",
                "amount": 500
            },
            "Tea Infusers": {
                "description": "Tea infusers for loose leaf tea brewing.",
                "amount": 30
            },
            "Lemon Slices": {
                "description": "Slices of fresh lemon for garnishing drinks.",
                "amount": 100
            },
            "Honey Packets": {
                "description": "Individual honey packets for sweetening tea and coffee.",
                "amount": 150
            },
            "Ice Scoops": {
                "description": "Ice scoops for adding ice to cold beverages.",
                "amount": 25
            },
            "Straws": {
                "description": "Plastic straws for cold drinks.",
                "amount": 1000
            },
            "Whipped Cream Dispenser": {
                "description": "Dispenser for whipped cream toppings.",
                "amount": 5
            },
            "Sugar Cubes": {
                "description": "Individual sugar cubes for coffee and tea.",
                "amount": 200
            },
            "Drink Napkins": {
                "description": "Small drink napkins for beverage service.",
                "amount": 800
            },
            "Reusable Coffee Filters": {
                "description": "Eco-friendly reusable coffee filters for sustainable brewing.",
                "amount": 30
            }
        }
    }

    return render(request, 'showsuppliesemployee.html', content)

# For Guest (no login)
@csrf_exempt
def order_food_ajax(request):
    if request.method == 'POST':
        food_name = request.POST.get("food_name")
        food_price = request.POST.get("food_price")
        amount = request.POST.get("amount")

        new_order = Order(food_name=food_name, food_price=food_price, amount=amount)
        new_order.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

# For Member (login)
@csrf_exempt
def order_food_ajax_member(request):
    if request.method == 'POST':
        user = request.user
        food_name = request.POST.get("food_name")
        food_price = request.POST.get("food_price")
        amount = request.POST.get("amount")

        new_order = OrderMember(user=user, food_name=food_name, food_price=food_price, amount=amount)
        new_order.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

# For Member (login)
@csrf_exempt
def borrow_book_member(request):
    if request.method == 'POST':
        id = request.POST.get("book")
        user = request.user
        book = Buku.objects.get(pk= id)

        new_order = BorrowedBook(user=user, book=book, borrowed=True)
        new_order.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

# For Member (login)
@csrf_exempt
def create_borrowed_history(request):
    if request.method == 'POST':
        book_id = request.POST.get("book")
        user = request.user
        book = Buku.objects.get(pk=book_id)
        
        # Check if the user has already borrowed a book with the same title
        existing_entry = BorrowedHistory.objects.filter(user=user, book__Judul=book.Judul).first()
        
        if existing_entry:
            # If an entry exists, update it
            existing_entry.book = book
            existing_entry.save()
        else:
            # If no entry exists, create a new one
            new_order = BorrowedHistory(user=user, book=book)
            new_order.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

# For Guest (no login)
@csrf_exempt
def delete_order_ajax(request, id):
    order = Order.objects.get(pk = id)
    if request.method == 'POST':
        order.delete()
        return HttpResponseRedirect(reverse('ordernborrow:show_order_guest'))
    
    return HttpResponseNotFound()

# For Member (login)
@csrf_exempt
def delete_order_ajax_member(request, id):
    order = OrderMember.objects.get(pk = id)
    if request.method == 'POST':
        order.delete()
        return HttpResponseRedirect(reverse('ordernborrow:show_order_member'))
    
    return HttpResponseNotFound()

# For Member (login)
@csrf_exempt
def return_book_member(request, id):
    book = Buku.objects.get(pk = id)
    borrowed = BorrowedBook.objects.filter(book=book)
    if request.method == 'POST':
        borrowed.delete()
        return HttpResponseRedirect(reverse('ordernborrow:show_order_member'))
    
    return HttpResponseNotFound()

# For Guest (no login)
@csrf_exempt
def delete_allorder_ajax(request):
    order = Order.objects.all()
    if request.method == 'POST':
        order.delete()
        return HttpResponseRedirect(reverse('ordernborrow:show_order_guest'))
    
    return HttpResponseNotFound()

# For Member (login)
@csrf_exempt
def delete_allorder_ajax_member(request):
    order = OrderMember.objects.filter(user = request.user)
    if request.method == 'POST':
        order.delete()
        return HttpResponseRedirect(reverse('ordernborrow:show_order_member'))
    
    return HttpResponseNotFound()

# For Guest (no login)
@csrf_exempt
def edit_order_ajax(request, id):
    if request.method == 'POST':
        try:
            order = Order.objects.get(pk=id)
            amount = request.POST.get("amount")
            order.amount = amount
            order.save()
            return JsonResponse({"message": "Order updated successfully"}, status=200)
        
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)

# For Member (login)
@csrf_exempt
def edit_order_ajax_member(request, id):
    if request.method == 'POST':
        try:
            order = OrderMember.objects.get(pk=id)
            amount = request.POST.get("amount")
            order.amount = amount
            order.save()
            return JsonResponse({"message": "Order updated successfully"}, status=200)
        
        except OrderMember.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
    
    return JsonResponse({"error": "Invalid request method"}, status=405)

# For Guest (no login)
def show_order_guest(request):
    orders = Order.objects.all()

    context = {
        'orders': orders
    }

    return render(request, "showorderguest.html", context)

# For Member (login)
def show_order_member(request):
    orders = OrderMember.objects.filter(user = request.user)

    context = {
        'orders': orders
    }

    return render(request, "showordermember.html", context)

# For Guest (no login)
def get_product_json(request):
    order_item = Order.objects.all()
    return HttpResponse(serializers.serialize('json', order_item))

# For Member (login)
def get_product_json_member(request):
    order_item = OrderMember.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', order_item))

# For Member (login)
def show_json_borrowedbooks(request):
    data = BorrowedBook.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# For Member (login)
def show_json_borrowedhistory(request):
    data = BorrowedHistory.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# For Member (login)
def show_books(request):
    data = Buku.objects.all()
    books = {
        'booklist': data
    }
    return render(request, "borrowbook.html", books)

# For Member (login)
def show_borrowed_books(request):
    current_user_id = request.user.id
    content = {
        'current_user_id': current_user_id,
    }
    return render(request, "returnbook.html", content)

# For Member (login)
def show_borrowed_history(request):
    current_user_id = request.user.id
    content = {
        'current_user_id': current_user_id,
    }
    return render(request, "borrowedhistory.html", content)