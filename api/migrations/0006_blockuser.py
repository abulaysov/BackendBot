# Generated by Django 4.0.5 on 2022-07-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_remove_userprofile_block"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlockUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("telegram_id", models.IntegerField()),
            ],
        ),
    ]
