from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Package, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Package.objects.all()
    query = None
    categories = None
    sort = None
    direction = None


    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products.html', context)
