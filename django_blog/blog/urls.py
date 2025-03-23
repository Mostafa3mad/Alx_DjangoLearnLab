from django.contrib.auth import views as auth_views
from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # custom views
    path('register/', blog_views.register, name='register'),
    path('profile/', blog_views.profile, name='profile'),
]
