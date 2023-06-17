from django.db import models
from django.urls import reverse

class Language(models.Model):
    # Field
    name = models.CharField(max_length=100)

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of 'ModelName'"""
        return reverse("language-detail", args=[str(self.id)])

    def __str__(self):
        return self.name

# # Create a new record using the model's constructor.
# record = Language(Language="Instance #1")

# # Save the object into the database.
# record.save()

# # Access model field values using Python attributes.
# print(record.id) # should return 1 for the first record.
# print(record.Language) # should print 'Instance #1'

# # Change record by modifying the fields, then calling save().
# record.Language = "New Instance Name"
# record.save()

# # Searching for records
# all_languages = Language.objects.all()

# # filter()
# english_language = Language.objects.filter(name__contains='English')
# number_english_language = english_language.count()
