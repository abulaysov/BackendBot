# Generated by Django 4.0.5 on 2022-06-11 13:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ("number_phone", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("group", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Schedules",
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
                ("first_monday", models.TextField(default="Поле не заполнено")),
                ("first_tuesday", models.TextField(default="Поле не заполнено")),
                ("first_wednesday", models.TextField(default="Поле не заполнено")),
                ("first_thursday", models.TextField(default="Поле не заполнено")),
                ("first_friday", models.TextField(default="Поле не заполнено")),
                ("first_saturday", models.TextField(default="Поле не заполнено")),
                ("second_monday", models.TextField(default="Поле не заполнено")),
                ("second_tuesday", models.TextField(default="Поле не заполнено")),
                ("second_wednesday", models.TextField(default="Поле не заполнено")),
                ("second_thursday", models.TextField(default="Поле не заполнено")),
                ("second_friday", models.TextField(default="Поле не заполнено")),
                ("second_saturday", models.TextField(default="Поле не заполнено")),
                ("third_monday", models.TextField(default="Поле не заполнено")),
                ("third_tuesday", models.TextField(default="Поле не заполнено")),
                ("third_wednesday", models.TextField(default="Поле не заполнено")),
                ("third_thursday", models.TextField(default="Поле не заполнено")),
                ("third_friday", models.TextField(default="Поле не заполнено")),
                ("third_saturday", models.TextField(default="Поле не заполнено")),
                ("fourth_monday", models.TextField(default="Поле не заполнено")),
                ("fourth_tuesday", models.TextField(default="Поле не заполнено")),
                ("fourth_wednesday", models.TextField(default="Поле не заполнено")),
                ("fourth_thursday", models.TextField(default="Поле не заполнено")),
                ("fourth_friday", models.TextField(default="Поле не заполнено")),
                ("fourth_saturday", models.TextField(default="Поле не заполнено")),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "schedules",
            },
        ),
    ]
