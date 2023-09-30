from django.urls import path
from .views import BookListView, BookDetailView

app_name = 'book'

urlpatterns = [
    path('list/', BookListView.as_view(), name='list'),
    path("show/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
]
