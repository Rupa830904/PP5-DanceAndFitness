from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import Review
from django.contrib.auth.models import User

class ReviewForm(forms.ModelForm):
    """ Form to ask a question"""
    class Meta:
        model = Review
        fields = ['product', 'rating', 'comment']
        rating = forms.IntegerField()
        comment = forms.CharField()

        labels = {
            'rating': 'rating',
            'comment': 'comment',
        }