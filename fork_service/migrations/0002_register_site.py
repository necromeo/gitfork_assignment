from django.contrib.sites.models import Site
from django.db import migrations

register_site = """INSERT INTO socialaccount_socialapp_sites
(socialapp_id, site_id) VALUES (1, 1);"""


def call_site(_, __):
    Site.objects.create(
        name="gitfork.com",
        domain="gitfork.com",
    )


class Migration(migrations.Migration):
    dependencies = [
        ("fork_service", "0001_create_github_provider"),
    ]

    operations = [
        migrations.RunPython(call_site, migrations.RunPython.noop),
        migrations.RunSQL(register_site),
    ]
