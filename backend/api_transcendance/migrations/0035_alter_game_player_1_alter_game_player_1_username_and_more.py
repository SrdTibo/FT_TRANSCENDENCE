# Generated by Django 5.0.4 on 2024-07-10 17:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_transcendance', '0034_name_tournaments_game_allowed_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player_1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_1_username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player_2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='player_2_username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
