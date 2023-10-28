from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import contact
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    """ Form to ask a question"""
    class Meta:
        model = contact
        fields = ['name', 'email', 'question']
        name = forms.CharField()
        question = forms.CharField()
        subscribe = forms.BooleanField()
        email = forms.CharField()

        labels = {
            'name': 'name',
            'email': 'Email',
            'question': 'question',
            'subscribr': 'subscribe',
        }

        def __init__(self, *args, **kwargs):
          super(ContactForm, self).__init__(*args, **kwargs)
          if self.instance and self.instance.subscribe is False:
              self.fields['email'].disabled = True # still displays the field in the template
            # del self.fields['job'] # removes field from form and template
          if self.instance and self.instance.subscribe is True:
              self.fields['email'].disabled = False
