# Generated by Django 3.1.1 on 2020-09-30 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0010_auto_20200930_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='album_cover/', verbose_name='Album cover'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='picture',
            field=models.ImageField(default='settings.MEDIA_ROOT/artist_picture/default-artist-placeholder.png', upload_to='artist_picture', verbose_name='Artist Picture'),
        ),
    ]
