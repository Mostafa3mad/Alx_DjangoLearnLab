# bookshelf/forms.py
from django import forms
from .models import Book  # استيراد نموذج الكتاب

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # ربط النموذج بـ Book
        fields = ['title', 'author', 'description']  # الحقول التي سيتم عرضها في النموذج

    # إضافة بعض التخصيصات إذا أردت
    title = forms.CharField(max_length=200, required=True)
    author = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)



from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
