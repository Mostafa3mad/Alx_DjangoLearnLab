from django.urls import include, path
from . import views
from .views import LoginView, LogoutView
from .views import list_books,LibraryDetailView
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),


    # Authentication URLs
    path('register/', views.register, name='register'),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # ✅ Built-in LogoutView

    path("admin-view/", admin_view, name="admin_view"),
    path("librarian-view/", librarian_view, name="librarian_view"),
    path("member-view/", member_view, name="member_view")

]