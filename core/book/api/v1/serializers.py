from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from book.models import Book, Genre, Writer


class WriterSerializer(ModelSerializer):
    class Meta:
        model = Writer
        fields = ["id", "name"]


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class BookSerializer(ModelSerializer):
    writer_name = ReadOnlyField(source='writer.name')
    genre = StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['id', 'name', 'genre', 'writer_name', 'writer', 'leaves', 'release_date']
