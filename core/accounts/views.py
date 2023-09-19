from django.contrib.auth.views import PasswordResetConfirmView, \
    PasswordResetView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from mail_templated import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .forms import SignUpForm, LoginForm
from .models import User
from .tokens import account_activation_token
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import logout, login
from django.utils.http import urlsafe_base64_decode


# Create your views here.

# signup view
class SignUpView(View):
    def get(self, request, *args, **kwargs):
        signup_form = SignUpForm()
        return render(request, 'accounts/signup.html', context={'form': signup_form})

    def post(self, request, *args, **kwargs):
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)

            send_mail('accounts/email/activation_account.tpl', context={
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            }, from_email='test@gmail.com', recipient_list=[user.email])

        return render(request, 'accounts/signup.html', context={'form': signup_form})


# account activation view
class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('home:home_page')
        else:

            return redirect('home:home_page')


# login view
class LoginView(View):
    def get(self, request, *args, **kwargs):
        login_form = LoginForm()
        return render(request, 'accounts/login.html', context={'form': login_form})

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_username = login_form.cleaned_data['username']
            user_password = login_form.cleaned_data['password']
            user = User.objects.filter(username__iexact=user_username).first()
            if user:
                if user.is_active:
                    is_correct_password = user.check_password(user_password)
                    if is_correct_password:
                        login(request, user)
                        return redirect('home:home_page')
                    else:
                        login_form.add_error('username', 'this user does not exist')
                else:
                    login_form.add_error('username', 'this user does not exist')
            else:
                login_form.add_error('username', 'this user does not exist')
            return render(request, 'accounts/login.html', context={'form': login_form})
        return redirect('home:home_page')


# logout view
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:login')


# password reset view
class CPasswordResetView(PasswordResetView):
    from_email = 'test@gmail.com'
    template_name = 'accounts/password_reset.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/email/reset_password_confirm.tpl'


# password reset done view
class PasswordResetDoneView(TemplateView):
    template_name = 'accounts/password_reset_done.html'


# password reset confirm view
class CPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


# password reset complete view
class PasswordResetCompleteView(TemplateView):
    template_name = 'accounts/password_reset_complete.html'
