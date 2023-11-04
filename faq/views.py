from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import ContactForm


def contact(request):

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
           contact_form.save()
           messages.success(request, 'Thanks for contacting us. we will get back to you soon')
    
    template = 'contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


# Create your views here.
