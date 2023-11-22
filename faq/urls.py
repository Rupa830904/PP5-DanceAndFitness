from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('about/', views.about_us, name='about'),
]
