# Generated by Django 3.1.2 on 2021-01-07 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobserver", "0056_swap_auto_now_add_for_defaulting_to_timezone_now"),
    ]

    operations = [
        migrations.AddField(
            model_name="stats",
            name="backend",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="stats",
                to="jobserver.backend",
            ),
        ),
    ]
