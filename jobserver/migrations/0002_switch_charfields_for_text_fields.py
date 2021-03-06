# Generated by Django 3.0.7 on 2020-09-30 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobserver", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="action_id",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="job",
            name="backend",
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="callback_url",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="status_message",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="joboutput",
            name="location",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="workspace",
            name="branch",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="workspace",
            name="db",
            field=models.TextField(
                choices=[
                    ("dummy", "Dummy database"),
                    ("slice", "Cut-down (but real) database"),
                    ("full", "Full database"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="workspace",
            name="name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="workspace",
            name="owner",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="workspace",
            name="repo",
            field=models.TextField(db_index=True),
        ),
    ]
