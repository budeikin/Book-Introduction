from django import forms
from .models import Rating


class BookRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['user', 'book', 'rating']
