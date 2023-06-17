from django.db import models
# from django.urls import reverse

class Genre(models.Model):
    # Field
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name

# # Create a new record using the model's constructor.
# record = Genre(Genre="Instance #1")

# # Save the object into the database.
# record.save()

# # Access model field values using Python attributes.
# print(record.id) # should return 1 for the first record.
# print(record.Genre) # should print 'Instance #1'

# # Change record by modifying the fields, then calling save().
# record.Genre = "New Instance Name"
# record.save()

# # Searching for records
# all_genres = Genre.objects.all()

# # filter()
# love_genre = Genre.objects.filter(name__contains='love')
# number_love_genre = love_genre.count()