from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, GenreSerializer, WriterSerializer
from book.models import Book, Genre, Writer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class WriterViewSet(ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().select_related('writer')
    serializer_class = BookSerializer
