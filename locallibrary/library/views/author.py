from django.shortcuts import render
from django.views import generic
from ..models.author import Author

class AuthorListView(generic.ListView):
    model = Author
    queryset = Author.objects.all()
    template_name = 'author_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
