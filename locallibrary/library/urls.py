from django.urls import path, re_path
from .views import views, author, book, book_instance

urlpatterns = [
    # http://127.0.0.1:8000/library/
    path('', views.index, name='index'),  # Home page

    # http://127.0.0.1:8000/library/books/
    path('books/', book.BookListView.as_view(), name='books'),  # List of all books

    # http://127.0.0.1:8000/library/authors/
    path('authors/', author.AuthorListView.as_view(), name='authors'),  # List of all authors

    # http://127.0.0.1:8000/library/book/1/
    path('book/<int:pk>/', book.BookDetailView.as_view(), name='book_detail'),  # The detail view for a particular book

    # http://127.0.0.1:8000/library/author/1/
    path('author/<int:pk>/', author.AuthorDetailView.as_view(), name='author_detail'),  # The detail view for a specific author

    # http://127.0.0.1:8000/library/bookinstances/
    path('bookinstances/', book_instance.BookInstanceListView.as_view(), name='bookinstances'),

    # http://127.0.0.1:8000/library/bookinstance/1/
    path('bookinstance/<int:pk>/', book_instance.BookInstanceDetailView.as_view(), name='bookinstance-detail'),

    # re_path permite utilizar expresiones regulares más complejas para especificar patrones de URL.
    # r'^book/(?P<pk>\d+)$
        # r Esto indica que se trata de una cadena de texto "raw" en Python, lo que significa que los caracteres especiales como \ no se tratarán como secuencias de escape.
        # ^: Coincide con el inicio de la cadena. Esto significa que la cadena debe comenzar exactamente con el texto "book/".
        # book/: Coincide con el texto literal "book/".
        # (?P<pk>\d+): Es una construcción de expresiones regulares llamada "grupos con nombre". Aquí, estamos creando un grupo llamado "pk" que coincide con uno o más dígitos (\d+).
        # $: Esto significa que la cadena debe terminar después del número entero.
    # http://127.0.0.1:8000/library/book/1
    re_path(r'^book/(?P<pk>\d+)$', book.BookDetailView.as_view(), name='book-detail'),
]
