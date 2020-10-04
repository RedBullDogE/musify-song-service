# Generated by Django 3.1.1 on 2020-09-30 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0008_auto_20200929_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='artist_picture', verbose_name='Artist Picture'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='songs.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.FileField(blank=True, null=True, upload_to='album_cover/', verbose_name='Album cover'),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop'), ('blues', 'Blues'), ('jazz', 'Jazz'), ('rockandroll', 'Rock&Roll'), ('folk', 'Folk'), ('hiphop', 'Hip Hop'), ('dance', 'Dance'), ('others', 'Others')], max_length=32, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Album'),
        ),
        migrations.AlterField(
            model_name='album',
            name='pub_year',
            field=models.IntegerField(verbose_name='Publication year'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='create_year',
            field=models.IntegerField(verbose_name='Creation year'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='genre',
            field=models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop'), ('blues', 'Blues'), ('jazz', 'Jazz'), ('rockandroll', 'Rock&Roll'), ('folk', 'Folk'), ('hiphop', 'Hip Hop'), ('dance', 'Dance'), ('others', 'Others')], max_length=32, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop'), ('blues', 'Blues'), ('jazz', 'Jazz'), ('rockandroll', 'Rock&Roll'), ('folk', 'Folk'), ('hiphop', 'Hip Hop'), ('dance', 'Dance'), ('others', 'Others')], max_length=32, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='pub_year',
            field=models.IntegerField(verbose_name='Publication year'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Song file'),
        ),
    ]
