from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from accounts.models import User


# Create your models here.

class Writer(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    slug = models.SlugField(null=True)
    image = models.ImageField(upload_to='writers/', null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_death = models.DateTimeField(null=True, blank=True)

    @property
    def birthdate(self):
        return self.date_of_birth.strftime('%Y')

    @property
    def deathdate(self):
        return self.date_of_death.strftime('%Y')

    def get_absolute_url(self):
        return reverse('book:writer_detail', args=[self.slug])

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to='books/', null=True, blank=True)
    genre = models.ManyToManyField(Genre, blank=True, related_name='books')
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='books')
    release_date = models.DateTimeField(null=True, blank=True)
    leaves = models.PositiveIntegerField()

    @property
    def yearpublished(self):
        return self.release_date.strftime('%Y')

    def get_absolute_url(self):
        return reverse('book:book_detail', args=[self.id])

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment_like = models.ManyToManyField(User, blank=True, related_name='com_like')
    total_like = models.PositiveIntegerField(default=0)

    @property
    def total_like(self):
        return self.comment_like.count()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.user.username
