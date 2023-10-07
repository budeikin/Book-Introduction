from django.contrib import admin
from .models import Writer, Genre, Book, Comment


# Register your models here.
class CommentAdminInline(admin.TabularInline):
    model = Comment
    extra = 1


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'writer']
    inlines = [CommentAdminInline]


class WriterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name", ]}


admin.site.register(Writer, WriterAdmin)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
