from django.db import models
from django.urls import reverse


# Create your models here.

class Writer(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    date_of_birth = models.DateTimeField(null=True, blank=True)
    date_of_death = models.DateTimeField(null=True, blank=True)

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