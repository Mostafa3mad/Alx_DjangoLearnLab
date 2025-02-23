from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Book
from .models import Library


def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/list_books.html"
    context_object_name = "library"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context


