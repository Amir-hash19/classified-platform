from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("accounts.api.urls")),
    path("api/", include("categories.api.urls")),
    path("api/", include("listings.api.urls")),
]
