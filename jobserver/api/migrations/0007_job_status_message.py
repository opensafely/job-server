# Generated by Django 3.0.7 on 2020-06-30 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200625_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status_message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]