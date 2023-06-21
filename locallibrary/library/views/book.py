from django.http import Http404
from django.shortcuts import render
from django.views import generic
from ..models.book import Book

class BookListView(generic.ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        search_word = self.request.GET.get('search', '')  # Get the search word from the query parameters
        queryset = Book.objects.filter(title__icontains=search_word)[:5]  # Get 5 books containing the search word
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_word = self.request.GET.get('search', '')  # Get the search word from the query parameters
        context['num_books'] = Book.objects.count()
        context['num_books_with_word'] = Book.objects.filter(title__icontains=search_word).count()
        return context

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    
    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')
        return render(request, 'catalog/book_detail.html', context={'book': book})
