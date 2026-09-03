from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from . import view

urlpatterns = [
    path("token/", TokenRefreshView.as_view(), name="token-refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token-verify"),
    path("login/", TokenObtainPairView.as_view(), name="login-user"),
    path("signup/", view.RegisterView.as_view(), name="register"),
]
