from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("fork_service.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
