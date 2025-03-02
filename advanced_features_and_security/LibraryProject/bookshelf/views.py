from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Book  # افترض أن لديك نموذجًا يسمى Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})



# bookshelf/views.py
from django.shortcuts import render
from .forms import ExampleForm  # تأكد من استيراد النموذج هنا

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)  # استخدام النموذج
        if form.is_valid():
            # التعامل مع البيانات المرسلة
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # تنفيذ أي عملية تحتاجها هنا
            return render(request, 'example_success.html', {'name': name, 'email': email})
    else:
        form = ExampleForm()

    return render(request, 'example_form.html', {'form': form})
