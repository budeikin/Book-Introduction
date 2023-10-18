from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from book.models import Writer, Book


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['latest_books'] = Book.objects.all().order_by('-id')[:4]
        return context


class AboutUsView(TemplateView):
    template_name = 'home/about_us_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = ContactForm
        return context


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'home/about_us_page.html'
    success_url = 'http://127.0.0.1:8000/about-us/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        email_message = EmailMessage(
            'Contact Form Submission from {}'.format(name),
            message,
            email,
            ["budeikin52@gmail.com", ],
        )
        email_message.send()
        return redirect('home:about_us_page')
