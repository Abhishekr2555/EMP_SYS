# Generated by Django 4.2.1 on 2023-07-19 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0014_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='otp',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='emp.user'),
        ),
    ]