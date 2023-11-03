from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Package, Category, Review
import pandas as pd
from .forms import ReviewForm
from django_pandas.io import read_frame

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
    # obj = Package.objects.all().first()
    num_reviews= product.num_of_reviews()
    rating= product.average_rating()
    reviews= product.show_reviews()
    df= read_frame(reviews,fieldnames=['comment'])
    #df= reviews.to_dataframe(['comment'], index_col=['reviews'])
    table_reviews = df.transpose().to_html()

    print(rating)
    print(df)
    print(reviews)

    context = {
        'product': product,
        'rating': rating,
        'num_reviews': num_reviews,
        'reviews': df,
    }

    return render(request, 'product_detail.html', context)

def review(request, package_id):
    
    product = get_object_or_404(Package, pk=package_id)
    review_form = ReviewForm() 
    
    template = 'product_review.html'
    context = {
        'product': product,
        'review_form': review_form,
    }

    return render(request, template, context)

