from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
    )

    phone_number = serializers.CharField(
        write_only=True, required=False, allow_blank=True
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "phone_number"]

    def create(self, validated_data):
        phone_number = validated_data.pop("phone_number", "")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
        )

        Profile.objects.create(user=user, phone_number=phone_number)

        return user
