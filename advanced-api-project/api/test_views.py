from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        """إعداد البيانات قبل كل اختبار"""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(title="Harry Potter", publication_year=2000, author=self.author)


    def test_create_book(self):
        """✅ اختبار إنشاء كتاب جديد"""
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_all_books(self):
        """✅ اختبار جلب جميع الكتب"""
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.json()), 1)  # تأكد أن هناك على الأقل كتاب واحد

    def test_get_single_book(self):
        """✅ اختبار جلب تفاصيل كتاب معين"""
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    def test_update_book(self):
        """✅ اختبار تحديث بيانات كتاب"""
        data = {"title": "Updated Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.put(f'/api/books/{self.book.id}/update/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """✅ اختبار حذف كتاب"""
        response = self.client.delete(f'/api/books/{self.book.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        """✅ اختبار تصفية الكتب حسب المؤلف"""
        response = self.client.get(f'/api/books/?author={self.author.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_search_books(self):
        """✅ اختبار البحث عن كتاب"""
        response = self.client.get('/api/books/?search=Harry')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_order_books_by_publication_year(self):
        """✅ اختبار ترتيب الكتب حسب سنة النشر"""
        response = self.client.get('/api/books/?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_unauthenticated_create_book(self):
        """✅ اختبار منع المستخدم غير المسجل من إنشاء كتاب"""
        self.client.logout()
        data = {"title": "Unauthorized Book", "publication_year": 2024, "author": self.author.id}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
