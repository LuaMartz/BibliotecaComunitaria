from django.db import models
from django.urls import reverse
# from .book import Book

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # books = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
    
# # Create a new record using the model's constructor.
# record = Author(Author="Instance #1")

# # Save the object into the database.
# record.save()

# # Access model field values using Python attributes.
# print(record.id) # should return 1 for the first record.
# print(record.Autho) # should print 'Instance #1'

# # Change record by modifying the fields, then calling save().
# record.Author = "New Instance Name"
# record.save()

# # Searching for records
# all_authors = Author.objects.all()

# # filter()
# juan_authors = Author.objects.filter(name__contains='Juan')
# number_juan_authors = juan_authors.count()
