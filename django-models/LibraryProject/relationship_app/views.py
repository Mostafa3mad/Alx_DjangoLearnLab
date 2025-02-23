from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library


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




#########################################################################
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect("home")  # Redirect to home page
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to home after login
    else:
        form = AuthenticationForm()

    return render(request, "relationship_app/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")  # Redirect to home after logout

# Protected Home Page (only logged-in users can access)
@login_required
def home_view(request):
    return render(request, "relationship_app/home.html")