from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class User(AbstractUser):
    # Fields
    name = models.CharField(max_length=100, blank=True, help_text='User Name')
    address = models.CharField(max_length=100, blank=True, help_text='User Direction')
    phone_number = models.PositiveIntegerField(null=True, blank=True, help_text='User Phone Number')
    id_user = models.PositiveIntegerField(null=True, blank=True, help_text='User ID')

    # Metadata
    class Meta:
        ordering = ['-User']
        orderind = ['-id_user']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of 'ModelName'"""
        return reverse("User_detail", args=[str(self.id)])
    
    def __str__(self):
        return self.username
    
# Create a new record using the model's constructor.
record = User(User="Instance #1")

# Save the object into the database.
record.save()

# Access model field values using Python attributes.
print(record.id) # should return 1 for the first record.
print(record.User) # should print 'Instance #1'

# Change record by modifying the fields, then calling save().
record.User = "New Instance Name"
record.save()

# Searching for records
all_users = User.objects.all()

# filter()
jhon_name_user = User.objects.filter(name__contains='Jhon')
number_jhon_name_user = jhon_name_user.count()