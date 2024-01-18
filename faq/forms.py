from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import Contact, Subscribe
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    """ Form to ask a question"""
    class Meta:
        model = Contact
        fields = ['name', 'subscribe', 'email', 'question']
        name = forms.CharField()
        question = forms.CharField()
        subscribe = forms.CheckboxInput()
        email = forms.CharField()

        labels = {
            'name': 'name',
            'email': 'Email',
            'question': 'question',
            'subscribe': 'Do you want to sunscribe our newsletters :',
        }

        def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            if self.instance and self.fields.subscribe is False:
                self.fields['email'].disabled = True
            if self.instance and self.fields.subscribe is True:
                self.fields['email'].disabled = False


class SubscribeForm(forms.ModelForm):
    """ Form to ask a question"""
    class Meta:
        model = Subscribe
        fields = ['name', 'email', ]
        name = forms.CharField()
        email = forms.CharField()

        labels = {
            'name': 'name',
            'email': 'Email',
        }
