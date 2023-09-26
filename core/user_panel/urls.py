from django.urls import path
from .views import DashboardView, ChangePasswordView, ChangePasswordDoneView,EditProfileView

app_name = 'user_panel'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('change-password/done/', ChangePasswordDoneView.as_view(), name='change_password_done'),
    path('edit-profile/', EditProfileView.as_view(), name='edit_profile'),

]
