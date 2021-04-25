from elasticsearch_dsl.query import MultiMatch
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from songs.serializers import (
    AlbumListSerializer,
    ArtistListSerializer,
    SongListSerializer,
)

from .documents import AlbumDocument, ArtistDocument, SongDocument


@api_view(["GET"])
@renderer_classes([BrowsableAPIRenderer, JSONRenderer])
def search_view(request):
    """View for fast searching in songs, albums and artists record using ElasticSearch API.

    Args:
        request (Request): GET request with searching query param

    Returns:
        Response: JSON response with found songs, albums and artists for specified query.
            Bad request if query param not specified.

    """
    searched_query = request.GET.get("q")
    if not searched_query:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    songs = SongDocument.search().query(
        MultiMatch(fields=["name", "artist.name", "album.name"], query=searched_query),
    )

    albums = AlbumDocument.search().query(
        MultiMatch(fields=["name", "artist.name"], query=searched_query),
    )

    artists = ArtistDocument.search().query(
        MultiMatch(fields=["name"], query=searched_query),
    )

    song_serializer = SongListSerializer(songs.to_queryset(), many=True)
    album_serializer = AlbumListSerializer(albums.to_queryset(), many=True)
    artist_serializer = ArtistListSerializer(artists.to_queryset(), many=True)

    data = {
        "results": {
            "songs": song_serializer.data,
            "albums": album_serializer.data,
            "artists": artist_serializer.data,
        }
    }

    return Response(data)
