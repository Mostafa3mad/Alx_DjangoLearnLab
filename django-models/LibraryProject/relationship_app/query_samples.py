from .models import Author,Book,Library,Librarian



def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def get_all_book_in_library(library_name):
        books = Library.objects.get(name=library_name).books.all()
        return books

def get_librarian(name_libraian):
    library = Librarian.objects.get(library=name_libraian)
    return library