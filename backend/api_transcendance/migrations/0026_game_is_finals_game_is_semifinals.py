# Generated by Django 5.0.4 on 2024-07-05 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_transcendance', '0025_remove_game_is_finish_remove_game_is_tournaments'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_finals',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='is_semifinals',
            field=models.BooleanField(default=False),
        ),
    ]
