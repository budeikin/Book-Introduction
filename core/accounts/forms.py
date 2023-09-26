from django import forms
from django.core.exceptions import ValidationError
from mail_templated import send_mail as send_maill, EmailMessage as Emailmessage
from .models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm


# Sign Up Form
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2',
        ]


# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(label='username or email', max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())


# Password Reset Form (customized email sender)
class CPasswordResetForm(PasswordResetForm):
    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        email_message = Emailmessage(email_template_name, context=context, from_email=from_email,
                                     recipient_list=[to_email, ])
        email_message.send()
