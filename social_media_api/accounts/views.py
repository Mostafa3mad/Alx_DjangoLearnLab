from rest_framework import generics, status, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import User as CustomUser
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



class FollowUserView(generics.GenericAPIView):
    """API to follow another user."""
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(self.get_queryset(), id=user_id)

        # Prevent self-following
        if user_to_follow == request.user:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user is already followed
        if request.user.is_following(user_to_follow):
            return Response({'detail': f'You are already following {user_to_follow.username}.'},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.follow(user_to_follow)
        return Response({'detail': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    """API to unfollow another user."""
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(self.get_queryset(), id=user_id)

        # Prevent self-unfollowing
        if user_to_unfollow == request.user:
            return Response({'detail': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user is not followed
        if not request.user.is_following(user_to_unfollow):
            return Response({'detail': f'You are not following {user_to_unfollow.username}.'},
                            status=status.HTTP_400_BAD_REQUEST)

        request.user.unfollow(user_to_unfollow)
        return Response({'detail': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)


class FollowersListView(generics.ListAPIView):
    """API to get the list of followers."""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.followers.all()


class FollowingListView(generics.ListAPIView):
    """API to get the list of users the authenticated user is following."""
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.following.all()