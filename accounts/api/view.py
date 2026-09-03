from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from . import serializers


class RegisterView(CreateAPIView):
    """user sign up

    Args:
        CreateAPIView (POST): send email, username, password, phone_number
    """

    serializer_class = serializers.RegisterSerializer
    permission_classes = [AllowAny]


class ProfileView(RetrieveAPIView):
    """get user profile

    Args:
        RetrieveAPIView (GET): must be authenticated

    Returns:
        Json: users profile
    """

    permission_classes = [IsAuthenticated]
    serializer_class = [serializers.ProfileSerializer]

    def get_object(self):
        return self.request.user.profile
