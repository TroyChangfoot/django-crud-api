from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):
    """Handles user registration and token creation."""
    password = serializers.CharField(write_only=True, min_length=6)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "token"]
        extra_kwargs = {"email": {"required": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user

    def get_token(self, obj):
        refresh = RefreshToken.for_user(obj)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
