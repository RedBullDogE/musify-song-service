from rest_framework import serializers

from .models import Song, Artist, Album


class ArtistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'genre', 'picture')


class SongListSerializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(slug_field='name', read_only=True)
    album = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Song
        fields = ('id', 'name', 'artist', 'genre', 'src', 'album')


class AlbumListSerializer(serializers.ModelSerializer):
    artist = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'artist', 'genre', 'cover')


class ArtistDetailSerializer(serializers.ModelSerializer):
    songs = SongListSerializer(
        read_only=True,
        many=True,
        source='top_songs'
    )

    albums = AlbumListSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Artist
        fields = '__all__'


class SongDetailSerializer(serializers.ModelSerializer):
    artist = ArtistListSerializer(read_only=True)

    class Meta:
        model = Song
        fields = '__all__'
