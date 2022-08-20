# Generated by Django 4.0.5 on 2022-08-20 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_customuser_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.group'),
        ),
    ]
