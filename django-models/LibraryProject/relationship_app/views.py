from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


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

