from rest_framework import generics, status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer,FollowSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
class FollowUserView(APIView):
    """API to follow another user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        if request.user.is_following(user_to_follow):
            return Response({'detail': 'You are already following this user.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.follow(user_to_follow)
        return Response({'detail': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)


class UnfollowUserView(APIView):
    """API to unfollow another user."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        if not request.user.is_following(user_to_unfollow):
            return Response({'detail': 'You are not following this user.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.unfollow(user_to_unfollow)
        return Response({'detail': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)


class FollowersListView(generics.ListAPIView):
    """API to get the list of followers."""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.followers.all()


class FollowingListView(generics.ListAPIView):
    """API to get the list of users the authenticated user is following."""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.following.all()