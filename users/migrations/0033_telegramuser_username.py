# Generated by Django 4.0.5 on 2022-09-10 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_telegramuser_is_moder'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='username',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
