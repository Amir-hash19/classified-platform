from django.contrib.auth.models import User
from rest_framework import serializers

from listings.models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            "id",
            "seller",
            "category",
            "title",
            "description",
            "price",
            "location",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "seller",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        return Listing.objects.create(
            seller=self.context["request"].user,
            **validated_data,
        )
