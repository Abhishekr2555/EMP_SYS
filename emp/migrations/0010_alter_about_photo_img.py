# Generated by Django 4.2.1 on 2023-07-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0009_alter_about_photo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_photo',
            name='img',
            field=models.ImageField(upload_to='static/imges'),
        ),
    ]
