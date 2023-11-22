from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Package
from django.contrib import messages

# Create your views here.

from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    
    product = Package.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url', 'view_cart')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Added {quantity} of {product.name} to your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

def remove_from_cart(request, item_id):
    """ Remove the specified product from the shopping cart """
    

    product = get_object_or_404(Package, pk=item_id)
    cart = request.session.get('cart', {})

    cart.pop(item_id)
    messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return render(request, 'cart.html')


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Package, pk=item_id)
    cart = request.session.get('cart', {})
    print(cart)
    quantity = cart.get(item_id)
    print(quantity)
    cart[item_id] = quantity
    
    return render(request, 'update_quantity.html')

   
def update_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    cart = request.session.get('cart', {})


    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        
        if item_id in list(cart.keys()):
            cart[item_id] = quantity

        request.session['cart'] = cart
        return redirect('view_cart')

    else:

        quantity = cart.get(item_id)
        cart[item_id] = quantity

        context = {
            'quantity': quantity
        }

        request.session['cart'] = cart
        return render(request, 'update_quantity.html', context)
