from .models import Author,Book,Library,Librarian


books_by_author = Book.objects.filter(author__name="J.K. Rowling")
books_in_library = Library.objects.get(name="Central Library").books.all()
librarian_for_library = Library.objects.get(name="Central Library").librarian
