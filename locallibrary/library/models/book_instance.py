from django.db import models
from .book import Book
import uuid # Required for unique book instances

class BookInstance(models.Model):
    # Fields
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200, help_text='Imprint Book Instance')
    uniqueld = models.CharField(max_length=250, help_text='Uniqueld Book Instance')
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'
    
# # Create a new record using the model's constructor.
# record = BookInstance(BookInstance="Instance #1")

# # Save the object into the database.
# record.save()

# # Access model field values using Python attributes.
# print(record.id) # should return 1 for the first record.
# print(record.BookInstance) # should print 'Instance #1'

# # Change record by modifying the fields, then calling save().
# record.BookInstance = "New Instance Name"
# record.save()

# # Searching for records
# all_book_instances = BookInstance.objects.all()

# # filter()
# pending_book_instance = BookInstance.objects.filter(status__contains='Pending')
# number_pending_book_instance = pending_book_instance.count()
