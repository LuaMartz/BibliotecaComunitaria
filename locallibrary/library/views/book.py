from django.views import generic
from ..models.book import Book

class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'