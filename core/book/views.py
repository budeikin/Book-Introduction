from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book, Writer, Genre


# Create your views here.

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/list_of_books.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.kwargs.get('id'):
            return qs.filter(genre__id=self.kwargs.get('id'))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['genres'] = Genre.objects.all()
        return context


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/detail_of_books.html'


class WritersListView(ListView):
    model = Writer
    context_object_name = 'writers'
    template_name = 'book/list_of_writers.html'


class WritersDetailView(DetailView):
    model = Writer
    slug_field = 'slug'
    template_name = 'book/detail_of_writers.html'
    context_object_name = 'writer'
