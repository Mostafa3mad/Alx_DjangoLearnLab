from django.contrib import admin

# Register your models here.
from .models import Author,Library,Librarian,Book

admin.site.register(Author)
admin.site.register(Librarian)
admin.site.register(Library)
admin.site.register(Book)