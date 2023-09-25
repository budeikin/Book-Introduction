from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from .forms import PasswordChangeForm


# Create your views here.

# dashboard view
class DashboardView(TemplateView):
    template_name = 'user_panel/dashboard.html'


# change password view
class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'user_panel/change_password.html'
    success_url = reverse_lazy('user_panel:change_password_done')


# change password done view
class ChangePasswordDoneView(TemplateView):
    template_name = 'user_panel/change_password_done.html'

# change information view
