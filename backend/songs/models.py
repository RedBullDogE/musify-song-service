from django.db import models
import uuid

GENRE_CHOICES = [
    ('rock', 'Rock'),
    ('pop', 'Pop'),
    ('blues', 'Blues'),
    ('jazz', 'Jazz'),
    ('rockandroll', 'Rock&Roll'),
    ('folk', 'Folk'),
    ('hiphop', 'Hip Hop'),
    ('dance', 'Dance'),
    ('others', 'Others'),
]


class Artist(models.Model):
    """Model definition for Artist."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField('Artist', max_length=64)
    genre = models.CharField('Genre', max_length=32, choices=GENRE_CHOICES)
    create_year = models.IntegerField('Creation year')
    picture = models.ImageField('Artist Picture', upload_to='artist_picture',
                                default='artist_picture/default-artist-placeholder.png')
    description = models.TextField(
        'Description', max_length=500, default='', blank=True)

    def top_songs(self):
        return Song.objects.all().filter(artist=self).order_by('popularity')[:5]

    class Meta:
        """Meta definition for Artist."""

        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField('Song', max_length=64)
    artist = models.ForeignKey(
        'Artist',
        on_delete=models.CASCADE,
        related_name='songs'
    )
    genre = models.CharField(
        'Genre',
        max_length=32,
        choices=GENRE_CHOICES
    )
    pub_year = models.IntegerField('Publication year')
    album = models.ForeignKey(
        'Album',
        on_delete=models.CASCADE,
        related_name='songs',
        blank=True,
        null=True
    )
    popularity = models.IntegerField('Number of song plays', default=0)
    src = models.FileField('Song file', blank=True,
                           null=True, upload_to='song_file')

    class Meta:
        """Meta definition for Song."""

        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.name


class Album(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField('Album', max_length=64)
    artist = models.ForeignKey(
        'Artist', on_delete=models.CASCADE, related_name='albums')
    genre = models.CharField('Genre', max_length=32, choices=GENRE_CHOICES)
    pub_year = models.IntegerField('Publication year')
    cover = models.ImageField('Album cover', blank=True,
                              null=True, upload_to='album_cover/')
    description = models.TextField('Description', default='', blank=True)

    class Meta:
        """Meta definition for Album."""

        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.name
