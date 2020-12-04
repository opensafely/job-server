# Generated by Django 3.1.2 on 2020-12-04 14:13

import base64
import secrets

from django.db import migrations


def new_id():
    """
    Return a random 16 character lowercase alphanumeric string
    We used to use UUID4's but they are unnecessarily long for our purposes
    (particularly the hex representation) and shorter IDs make debugging
    and inspecting the job-runner a bit more ergonomic.

    COPIED FROM jobserver/models.py at c2da636
    """
    return base64.b32encode(secrets.token_bytes(10)).decode("ascii").lower()


def add_dummy_identifiers(apps, schema_editor):
    Job = apps.get_model("jobserver", "Job")

    for job in Job.objects.filter(identifier=""):
        job.identifier = f"{new_id()}-manually-set"
        job.save()


def remove_dummy_identifiers(apps, schema_editor):
    Job = apps.get_model("jobserver", "Job")

    Job.objects.filter(identifier__endswith="-dummy").update(identifier="")


class Migration(migrations.Migration):

    dependencies = [
        ("jobserver", "0034_remove_job_output"),
    ]

    operations = [
        migrations.RunPython(
            add_dummy_identifiers, reverse_code=remove_dummy_identifiers
        )
    ]