from django.views import generic
from ..models.genre import Genre
from ..models.book import Book

class GenreListView(generic.ListView):
    model = Genre
    queryset = Genre.objects.all()
    template_name = 'genre_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_word = self.request.GET.get('search', '')  # Get the search word from the query parameters
        context['num_genres'] = Genre.objects.count()
        context['num_books_with_word'] = Book.objects.filter(title__icontains=search_word).count()
        return context
class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = 'genre_detail.html'