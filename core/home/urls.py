from django.urls import path
from .views import HomeView,AboutUsView,ContactView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('about-us/', AboutUsView.as_view(), name='about_us_page'),
    path('contact-us/', ContactView.as_view(), name='contact_us_page'),
]
