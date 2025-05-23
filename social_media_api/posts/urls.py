from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LikePostView,
    UnlikePostView,
    PostViewSet,
    CommentViewSet,
    FeedView,
)
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
    path('feed/', FeedView.as_view(), name='user-feed'),
]
