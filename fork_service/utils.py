from typing import Union

from allauth.socialaccount.models import SocialAccount


def get_user_url(user: str) -> Union[None, str]:
    try:
        social_user = SocialAccount.objects.get(user__username=user)
    except SocialAccount.DoesNotExist:
        return None

    user_url: str = social_user.extra_data.get("html_url")

    return user_url
