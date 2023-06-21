from django.urls import path
from .views import views, author, book, book_instance

urlpatterns = [
    # http://127.0.0.1:8000/library
        # Home page
    path('', views.index, name = "index"), 
]

urlpatterns += [
    # http://127.0.0.1:8000/books
    path('books/', book.BookListView.as_view(), name='books'), # List of all books

    # http://127.0.0.1:8000/authors
    path('authors/', author.AuthorListView.as_view(), name='authors'), # List of all authors
     
    # http://127.0.0.1:8000/book/1
    path('book/<int:pk>', book.BookDetailView.as_view(), name='book_detail'), # The detail view for a particular book, with a field primary key of <id> (the default).
       
    # http://127.0.0.1:8000/author/1
    path('author/<int:pk>', author.AuthorDetailView.as_view(), name='author_detail'), # The detail view for the specific author with a primary key field of <id>.

    # http://127.0.0.1:8000/bookinstances
    path('bookinstances/', book_instance.BookInstanceListView.as_view(), name='bookinstances'),
    
    # http://127.0.0.1:8000/bookinstances/1
    path('bookinstance/<int:pk>/', book_instance.BookInstanceDetailView.as_view(), name='bookinstance-detail'),
]