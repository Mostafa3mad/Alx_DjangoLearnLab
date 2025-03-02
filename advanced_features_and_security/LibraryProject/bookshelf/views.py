from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Book  # افترض أن لديك نموذجًا يسمى Book

@permission_required('bookshelf.can_view', raise_exception=True)  # التحقق من التصريح
def book_list(request):
    # جلب جميع الكتب من قاعدة البيانات
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
