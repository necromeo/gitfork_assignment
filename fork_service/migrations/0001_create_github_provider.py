import os
from pathlib import Path

import environ
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site
from django.db import migrations

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


def add_git_hub_provider(_, __):
    SocialApp.objects.create(
        provider="github",
        name="GitHub",
        client_id=env.str("CLIENT_ID"),
        secret=env.str("CLIENT_SECRET"),
    )


class Migration(migrations.Migration):

    dependencies = [
        ("socialaccount", "0003_extra_data_default_dict"),
        ("sites", "0002_alter_domain_unique"),
        ("sessions", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_git_hub_provider, migrations.RunPython.noop),
    ]
