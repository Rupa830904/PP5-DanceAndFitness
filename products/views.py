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
    category = None
    sort = None
    direction = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            #if sortkey == 'name':
             #   sortkey = 'lower_name'
              #  products = products.annotate(lower_name=Lower('name'))
            #if sortkey == 'category':
             #   sortkey = 'category__name'
            #if 'direction' in request.GET:
             #   direction = request.GET['direction']
              #  if direction == 'desc':
               #     sortkey = f'-{sortkey}'
            products = products.order_by(sort)

        if 'category' in request.GET:
                category = request.GET['category']
                products = products.filter(category__name=category)
                category = Category.objects.filter(name=category)

        if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search!")
                    return redirect(reverse('products'))
            
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)
        


    context = {
        'products': products,
        'search_term': query,
        'current_category': category,
    }

    return render(request, 'products.html', context)

def product_detail(request, package_id):
    """ A view to show individual product details """

    product = get_object_or_404(Package, pk=package_id)

    context = {
        'product': product,
    }

    return render(request, 'product_detail.html', context)
