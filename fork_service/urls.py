from django.urls import path
from django.views.generic import RedirectView

from .views import fork_repo, home, result

urlpatterns = [
    path("", RedirectView.as_view(url="home/")),
    path("home/", home, name="home"),
    path("fork/", fork_repo, name="fork"),
    path("result/", result, name="result"),
]
