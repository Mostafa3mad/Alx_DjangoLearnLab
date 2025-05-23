from django.urls import path
from .views import(
    RegisterView,
    LoginView,
    ProfileView,
    FollowUserView,
    UnfollowUserView,
    FollowersListView,
    FollowingListView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Follow and Unfollow endpoints

    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),

    # List followers and following users
    path('followers/', FollowersListView.as_view(), name='followers-list'),
    path('following/', FollowingListView.as_view(), name='following-list'),
]
