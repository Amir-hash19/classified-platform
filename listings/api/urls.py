from django.urls import path

from . import views

urlpatterns = [
    path(
        "list/",
        views.ListingListCreateView.as_view(),
        name="listing-list-create",
    ),
    path(
        "list/<int:pk>/",
        views.ListingRetrieveUpdateView.as_view(),
        name="listing-retrieve-update",
    ),
    path(
        "list/<int:pk>/delete/",
        views.ListingRetrieveDestroyView.as_view(),
        name="listing-retrieve-destroy",
    ),
]