# Generated by Django 4.2.1 on 2023-07-19 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0015_profile_mobile_profile_otp_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
