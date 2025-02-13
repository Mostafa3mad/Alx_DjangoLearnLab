# استرجاع جميع الكتب من قاعدة البيانات

```python
from bookshelf.models import Book
 books = Book.objects.get(title='1984')


