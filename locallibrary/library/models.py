from django.db import models
from django.urls import reverse

# Create your models here.

class BookModel(models.Model):
    title = models.CharField(max_length=200, help_text='Book title')
    author = models.
    summary = models.CharField(max_length=200, help_text='Summary book')

