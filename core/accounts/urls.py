from django.urls import path
from .views import SignUpView, ActivateAccountView, ActivationAccountDoneView, LoginView, LogoutView, \
    CPasswordResetView, CPasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordResetDoneView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),
    path('activate/done/', ActivationAccountDoneView.as_view(), name='activate_done'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', CPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', CPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
