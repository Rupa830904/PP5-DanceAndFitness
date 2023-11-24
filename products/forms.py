from django import forms
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import Review, Package
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


class ProductForm(forms.ModelForm):
    """ Form to ask a question"""
    class Meta:
        model = Package
        fields = ['category', 'name', 'price', 'description', 'package_image']
        name = forms.CharField()
        description = forms.CharField()
        price = forms.DecimalField()

        labels = {
            'name': 'name',
            'price': 'price',
        }


class Editproduct(forms.ModelForm):
    """ Form to ask a question"""
    class Meta:
        model = Package
        fields = ['price', 'description']
        description = forms.CharField()
        price = forms.DecimalField()

        labels = {
            'description': 'description',
            'price': 'price',
        }
