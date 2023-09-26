from accounts.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from .forms import PasswordChangeForm, EditProfileForm
from django.contrib.auth import settings


# Create your views here.

# dashboard view
class DashboardView(TemplateView):
    template_name = 'user_panel/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['profile'] = UserProfile.objects.get(id=self.request.user.id)
        return context


# change password view
class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'user_panel/change_password.html'
    success_url = reverse_lazy('user_panel:change_password_done')


# change password done view
class ChangePasswordDoneView(TemplateView):
    template_name = 'user_panel/change_password_done.html'


# dashboard menu component
def profile_menu_component(request):
    return render(request, 'user_panel/components/user_panel_menu.html')


# edit profile view
class EditProfileView(View):
    def get(self, request, **kwargs):
        current_user = request.user
        edit_profile_form = EditProfileForm(instance=current_user)
        return render(request, 'user_panel/edit_profile.html', context={'form': edit_profile_form})

    def post(self, request):
        current_user = request.user
        edit_profile_form = EditProfileForm(request.POST, instance=current_user)
        if edit_profile_form.is_valid():
            edit_profile_form.save()
        return render(request, 'user_panel/edit_profile.html', context={'form': edit_profile_form})
