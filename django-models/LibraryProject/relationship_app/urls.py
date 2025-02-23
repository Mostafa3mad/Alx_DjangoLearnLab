from django.urls import include, path
from . import views
from .views import LoginView, LogoutView
from .views import list_books,LibraryDetailView
urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),


    # Authentication URLs
    path('register/', views.register, name='register'),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # ✅ Built-in LogoutView
]