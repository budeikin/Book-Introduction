from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True, validators=[EmailValidator()])
    message = forms.CharField(widget=forms.Textarea)
