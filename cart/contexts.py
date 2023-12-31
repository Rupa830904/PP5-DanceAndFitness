from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Package


def cart_contents(request):

    cart_items = []
    total = 0
    package_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Package, pk=item_id)
        total += quantity * product.price
        package_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'package_count': package_count,
    }

    return context
