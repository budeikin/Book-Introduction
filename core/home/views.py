from django.shortcuts import render
from django.views.generic import TemplateView
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
