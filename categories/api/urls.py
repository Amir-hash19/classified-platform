from django.urls import path

from .views import (
    CategoryListCreateView,
    CategoryRetrieveDestroyView,
    CategoryRetrieveUpdateView,
)

urlpatterns = [
    path(
        "category/",
        CategoryListCreateView.as_view(),
        name="category-list-create",
    ),
    path(
        "category/<int:pk>/",
        CategoryRetrieveUpdateView.as_view(),
        name="category-retrieve-update",
    ),
    path(
        "category/<int:pk>/delete/",
        CategoryRetrieveDestroyView.as_view(),
        name="category-retrieve-destroy",
    ),
]