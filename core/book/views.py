from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book, Writer, Genre, Comment
from .forms import CommentForm


# Create your views here.

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/list_of_books.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if self.kwargs.get('id'):
            return qs.filter(genre__id=self.kwargs.get('id'))
        elif self.kwargs.get('slug'):
            return qs.filter(writer__slug=self.kwargs.get('slug'))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['genres'] = Genre.objects.all()
        context['writers'] = Writer.objects.all()
        return context


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/detail_of_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        comment_form = CommentForm()
        context['comments'] = Comment.objects.filter(book_id=self.object.id)
        context['comment_form'] = comment_form
        return context


class WritersListView(ListView):
    model = Writer
    context_object_name = 'writers'
    template_name = 'book/list_of_writers.html'


class WritersDetailView(DetailView):
    model = Writer
    slug_field = 'slug'
    template_name = 'book/detail_of_writers.html'
    context_object_name = 'writer'


class CommentCreateView(View):
    def post(self, request, id):
        url = request.META.get('HTTP_REFERER')
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            book = Book.objects.get(id=id)
            form.instance.user = request.user
            form.instance.book = book
            form.save()

        return redirect(url)


class CommentLike(View, LoginRequiredMixin):
    def get(self, request, id):
        url = request.META.get('HTTP_REFERER')
        comment = get_object_or_404(Comment, id=id)
        if comment.comment_like.filter(id=request.user.id).exists():
            comment.comment_like.remove(request.user)
        else:
            comment.comment_like.add(request.user)

        return redirect(url)
