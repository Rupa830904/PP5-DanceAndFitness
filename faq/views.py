from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import ContactForm, SubscribeForm


def contact(request):

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thanks for contacting us.')

    template = 'contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


def about_us(request):
    """ A view that renders the cart contents page """

    return render(request, 'about_us.html')

def subscribe(request):

    subscribe_form = SubscribeForm()

    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            messages.success(request, 'Thanks for subscribing us.')

    template = 'subscribe.html'
    context = {
        'subscribe_form': subscribe_form,
    }

    return render(request, template, context)

