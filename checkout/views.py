from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))
    
    current_cart = cart_contents(request)
    total = current_cart('total')
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O5au8LpwurLjjCDYB8YIkXPazNfmWvgG0X7uVyisncqHg9dRvnEyZ9r4JZR9sgztIZzOuMeaP1sapyzkGEKGpeL00tAMMTXiC',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
