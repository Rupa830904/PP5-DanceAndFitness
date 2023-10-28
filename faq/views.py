from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import ContactForm


def contact(request):

    contact_form = ContactForm() 
    
    template = 'contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


# Create your views here.
