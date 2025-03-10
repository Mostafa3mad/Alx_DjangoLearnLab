from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics,viewsets
from .models import Book

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet (viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

