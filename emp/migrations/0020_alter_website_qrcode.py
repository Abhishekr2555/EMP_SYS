# Generated by Django 4.2.1 on 2023-07-29 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0019_alter_website_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='qrcode',
            field=models.ImageField(blank=True, upload_to='staticfiles/media/media/'),
        ),
    ]
