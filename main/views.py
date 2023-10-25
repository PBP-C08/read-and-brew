from main.models import Profile, Order
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect
from main.forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers


def show_main(request):
    return render(request, "main.html")

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("main:show_main")) # membuat response
            return response
        else:
            messages.info(request, 'Invalid username/password!')
            
    context = {'form':form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = redirect('main:show_main')
    return response

def signup(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(
                user = new_user,
                status = new_user.status,
                full_name = new_user.full_name,
                email = new_user.email
                )
            messages.success(request, 'Sign up successful!')
            return redirect('main:login')
    
    context = {'form':form}
    return render(request, 'signup.html', context)

def show_json(request):
    data = Order.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Order.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# for guest (no login)
def food_view(request):
    content = {
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

# for guest (no login)
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

# for guest (no login)
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

# for guest (no login)
@csrf_exempt
def delete_order_ajax(request, id):
    order = Order.objects.get(pk = id)
    if request.method == 'POST':
        order.delete()
        return HttpResponseRedirect(reverse('main:show_order_guest'))
    
    return HttpResponseNotFound()

# for guest (no login)
@csrf_exempt
def delete_allorder_ajax(request):
    order = Order.objects.all()
    if request.method == 'POST':
        order.delete()
        return HttpResponseRedirect(reverse('main:show_order_guest'))
    
    return HttpResponseNotFound()

# for guest (no login)
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

# for guest (no login)
def show_order_guest(request):
    orders = Order.objects.all()

    context = {
        'orders': orders
    }

    return render(request, "showorderguest.html", context)

# for guest (no login)
def get_product_json(request):
    order_item = Order.objects.all()
    return HttpResponse(serializers.serialize('json', order_item))