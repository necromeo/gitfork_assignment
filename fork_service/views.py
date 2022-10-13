import logging

import requests
from allauth.socialaccount.models import SocialToken
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.html import format_html

from .utils import get_user_url

log = logging.getLogger(__name__)


def home(request):
    return render(request, "home.html")


def fork_repo(request):
    user = request.user
    gh_token = SocialToken.objects.get(account_id__user_id__username=user)
    user_url = get_user_url(user)
    headers = {
        "Authorization": f"Bearer {gh_token}",
        "Accept": "application/vnd.github+json",
    }
    data = {
        "name": f"Forked-{settings.REPO}",
        "default_branch_only": False,
    }

    try:
        req = requests.post(
            f"https://api.github.com/repos/{settings.OWNER}/{settings.REPO}/forks",
            headers=headers,
            json=data,
            timeout=30,
        )

    except requests.exceptions.Timeout:
        log.error("Forking timed out")

    except Exception as e:
        log.error(f"Forking exception: {e}")
    else:
        if req.status_code >= 400:
            log.error(f"Forking failed: {req.text}")
            messages.error(request, "There was an error forking the repository.")
        else:
            messages.info(request, "Repo is being forked...")

    request.session["user_repo"] = user_url

    return redirect(reverse("result"))


def result(request):
    user_repo = request.session.pop("user_repo", "")
    return render(
        request, "result.html", context={"repo": user_repo, "user": request.user}
    )
