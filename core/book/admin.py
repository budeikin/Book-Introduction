from django.contrib import admin
from .models import Writer, Genre, Book

# Register your models here.

admin.site.register(Writer)
admin.site.register(Genre)
admin.site.register(Book)
