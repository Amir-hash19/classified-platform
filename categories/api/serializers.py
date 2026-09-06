from django.contrib.auth.models import User
from rest_framework import serializers
from categories.models import  Category






class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "parent",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]