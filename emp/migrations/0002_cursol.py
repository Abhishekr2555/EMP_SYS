# Generated by Django 4.2.1 on 2023-06-29 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cursol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=200)),
            ],
        ),
    ]