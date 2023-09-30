from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book


# Create your views here.

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/list_of_books.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/detail_of_books.html'
