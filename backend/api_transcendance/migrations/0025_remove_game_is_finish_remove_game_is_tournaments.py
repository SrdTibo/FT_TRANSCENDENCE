# Generated by Django 5.0.4 on 2024-07-05 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_transcendance', '0024_game_is_tournaments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='is_finish',
        ),
        migrations.RemoveField(
            model_name='game',
            name='is_tournaments',
        ),
    ]
