# Generated by Django 3.2 on 2021-04-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_usersong'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersong',
            name='song',
        ),
        migrations.AddField(
            model_name='usersong',
            name='song',
            field=models.ManyToManyField(to='songs.Song'),
        ),
    ]
