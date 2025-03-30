from rest_framework import viewsets, permissions, filters,generics
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from notifications.utils import create_notification

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post_id = self.request.query_params.get('post')
        if post_id:
            return Comment.objects.filter(post_id=post_id).order_by('-created_at')
        return Comment.objects.all().order_by('-created_at')



class FeedView(generics.ListAPIView):
    """API to get posts from followed users."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the list of followed users
        following_users = self.request.user.following.all()

        # Fetch posts from followed users ordered by creation date
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikePostView(generics.GenericAPIView):
    """API to like a post."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        # Check if the post is already liked
        like, created = Like.objects.get_or_create(post=post, user=request.user)

        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post author
        if request.user != post.author:
            create_notification(post.author, request.user, 'liked', post)

        return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    """API to unlike a post."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(post=post, user=request.user)

        if like.exists():
            like.delete()
            return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)

        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)