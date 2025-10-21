from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from django.contrib.auth.models import User


class RegisterView(generics.CreateAPIView):
    """Public endpoint for registering a new user."""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class AccountView(APIView):
    """Account View for logged in user"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })
