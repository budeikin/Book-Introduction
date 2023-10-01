from django.contrib import admin
from .models import Writer, Genre, Book


# Register your models here.

class WriterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name", ]}


admin.site.register(Writer, WriterAdmin)
admin.site.register(Genre)
admin.site.register(Book)
