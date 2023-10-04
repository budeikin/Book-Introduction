from django.urls import path,include
from .views import BookListView, BookDetailView, WritersListView, WritersDetailView

app_name = 'book'

urlpatterns = [
    path('list/', BookListView.as_view(), name='list'),
    path('list/<int:id>/', BookListView.as_view(), name='list_by_genre'),
    path("show/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path('writers/', WritersListView.as_view(), name='writers_list'),
    path("writers/<slug:slug>/", WritersDetailView.as_view(), name="writer_detail"),

]
