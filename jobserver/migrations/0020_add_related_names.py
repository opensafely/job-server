# Generated by Django 3.1.2 on 2020-11-05 10:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobserver", "0019_remove_nullability_from_text_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="needed_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="children",
                to="jobserver.job",
            ),
        ),
        migrations.AlterField(
            model_name="jobrequest",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="job_requests",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="workspace",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="workspaces",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
