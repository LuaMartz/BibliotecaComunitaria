from django.shortcuts import render
from django.views import generic
from ..models.book_instance import BookInstance

class BookInstanceListView(generic.ListView):
    model = BookInstance
    template_name = 'bookinstance_list.html'

class BookInstanceDetailView(generic.DetailView):
    model = BookInstance
    template_name = 'bookinstance_detail.html'
