# Generated by Django 5.0.4 on 2024-05-14 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_transcendance', '0006_user_otp_user_otp_expiry_time_delete_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number_user',
        ),
    ]
