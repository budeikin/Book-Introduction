from django.shortcuts import render
from django.views.generic import TemplateView

from book.models import Writer


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        writer = Writer.objects.get(id=1)
        context['books'] = writer.books.all()
        return context
