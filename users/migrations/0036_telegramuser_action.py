# Generated by Django 4.0.5 on 2022-10-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_groupusertelegram_owner_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='action',
            field=models.CharField(blank=True, choices=[('PTY', 'PairsToday'), ('PTW', 'PairsTomorrow')], max_length=255, null=True),
        ),
    ]
