from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
)

from listings.models import Listing

from . import permissions, serializers


class ListingListCreateView(ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = serializers.ListingSerializer
    permission_classes = [permissions.IsOwnerOrStaffOrSuperuser]


class ListingRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = serializers.ListingSerializer
    permission_classes = [permissions.IsOwnerOrStaffOrSuperuser]


class ListingRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = serializers.ListingSerializer
    permission_classes = [permissions.IsOwnerOrStaffOrSuperuser]
