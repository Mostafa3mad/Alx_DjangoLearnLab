# api/serializers.py
from rest_framework import serializers  # Make sure to import serializers from DRF
from .models import Book  # Import your Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Specify the model to serialize
        fields = '__all__'  # Include all fields of the Book model
