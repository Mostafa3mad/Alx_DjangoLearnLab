# استرجاع جميع الكتب من قاعدة البيانات

```python
books = Book.objects.all()
for book in books:
    print(book)
