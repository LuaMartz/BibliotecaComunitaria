from django.views import generic
from ..models.book import Book

class BookListView(generic.ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'templates/library/book_list.html'
    context_object_name = 'books'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    
    def get_queryset(self):
        return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        search_word = self.request.GET.get('search', '')  # Get the search word from the query parameters
        context['num_books'] = Book.objects.count()
        context['num_books_with_word'] = Book.objects.filter(title__icontains=search_word).count()
        return context

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'