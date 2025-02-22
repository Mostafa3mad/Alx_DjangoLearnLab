from .models import Author,Book,Library,Librarian



def get_books_by_author(author_name):
    try:
        books = Book.objects.filter(author=Author.objects.get(name="J.K. Rowling"))
    except Author.DoesNotExist:
        return None
def get_all_book_in_library(name_library):
    try:
        books_inlibrary = Library.objects.get(name=name_library).books.all()

    except Librarian.DoesNotExist:
        return None

def get_librarian(name_libraian):
    quary = Librarian.objects.get(name=name_libraian).librarian
