# Generated by Django 3.1.1 on 2020-09-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0012_auto_20200930_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='picture',
            field=models.ImageField(default='artist_picture/default-artist-placeholder.png', upload_to='artist_picture', verbose_name='Artist Picture'),
        ),
    ]
