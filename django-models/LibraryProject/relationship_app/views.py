from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import  user_passes_test

def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user after registration
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


class LoginView(BaseLoginView):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True  # Redirect if the user is already authenticated

# Logout View
class LogoutView(BaseLogoutView):
    template_name = 'relationship_app/logout.html'

##############################################################################

# Function to check if the user is an Admin
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')  # ✅ Corrected path


# Function to check if the user is a Librarian
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')  # ✅ Corrected path


# Function to check if the user is a Member
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')  # ✅ Corrected path
##############################################################################
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from django.contrib.auth.decorators import permission_required
# ✅ Secure Add Book View
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')  # Assuming author_id is sent from a form
        book = Book.objects.create(title=title, author_id=author_id)
        return redirect('list_books')
    return render(request, "relationship_app/add_book.html")  # Render a simple form page

# ✅ Secure Edit Book View
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get('title', book.title)
        book.author_id = request.POST.get('author_id', book.author.id)  # Keep existing author if not changed
        book.save()
        return redirect('list_books')
    return render(request, "relationship_app/edit_book.html", {"book": book})

# ✅ Secure Delete Book View
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, "relationship_app/delete_book.html", {"book": book})
