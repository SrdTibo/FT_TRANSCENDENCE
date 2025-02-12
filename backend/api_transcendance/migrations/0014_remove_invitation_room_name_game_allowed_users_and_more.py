# Generated by Django 5.0.4 on 2024-06-06 08:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_transcendance', '0013_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='room_name',
        ),
        migrations.AddField(
            model_name='game',
            name='allowed_users',
            field=models.ManyToManyField(related_name='rooms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='jwt_access',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='jwt_refresh',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
