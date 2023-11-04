from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<package_id>', views.product_detail, name='product_detail'),
    path('<package_id>/reviews', views.review, name='review'),
    path('add/', views.add_product, name='add_product'),
]