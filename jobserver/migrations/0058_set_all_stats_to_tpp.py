# Generated by Django 3.1.2 on 2021-01-07 14:54

from django.db import migrations


def set_all_stats_backend_to_tpp(apps, schema_editor):
    Backend = apps.get_model("jobserver", "Backend")
    Stats = apps.get_model("jobserver", "Stats")

    tpp = Backend.objects.get(name="tpp")
    Stats.objects.update(backend=tpp)


def unset_all_stats_backends(apps, schema_editor):
    Stats = apps.get_model("jobserver", "Stats")

    Stats.objects.update(backend=None)


class Migration(migrations.Migration):

    dependencies = [
        ("jobserver", "0057_link_stats_to_backend"),
    ]

    operations = [
        migrations.RunPython(
            set_all_stats_backend_to_tpp, reverse_code=unset_all_stats_backends
        )
    ]