from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


# Sign Up Form
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2',
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
