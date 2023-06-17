from django.db import models
from django.urls import reverse
from .genre import Genre
from .language import Language
from .author import Author

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField(max_length=13, unique=True, help_text='13 Character ISBN number')
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ManyToManyField(Language, help_text='Select a language for this book')
    
    # Methods
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of 'ModelName'"""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'
