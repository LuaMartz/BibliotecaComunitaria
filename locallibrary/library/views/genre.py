from django.views import generic
from ..models.genre import Genre

class GenreListView(generic.ListView):
    model = Genre
    queryset = Genre.objects.all()
    template_name = 'genre_list.html'

class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = 'genre_detail.html'