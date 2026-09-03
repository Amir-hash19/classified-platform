from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
    )

    phone_number = serializers.CharField(
        write_only=True, required=False, allow_blank=True
    )

    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "phone_number", "access", "refresh"]

    def create(self, validated_data):
        phone_number = validated_data.pop("phone_number", "")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )

        Profile.objects.create(user=user, phone_number=phone_number)

        refresh = RefreshToken.for_user(user)

        user.access = str(refresh.access_token)
        user.refresh = str(refresh)

        return user


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Profile

        fields = ["username", "email", "phone_number"]
