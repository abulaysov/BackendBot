# Generated by Django 4.0.5 on 2023-01-04 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0017_schedule_end_time_schedule_start_time"),
    ]

    operations = [
        migrations.DeleteModel(
            name="NumberWeek",
        ),
    ]
