from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Album, Artist, Song, UserSongs
from .serializers import (
    AlbumDetailSerializer,
    ArtistDetailSerializer,
    SongDetailSerializer,
    SongListSerializer,
)


class LibraryPagePagination(PageNumberPagination):
    page_size = 10
    page_query_param = "page"


class LibraryView(ListAPIView):
    serializer_class = SongListSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LibraryPagePagination

    def get_queryset(self):
        user_id = self.request.user.id
        return Song.objects.filter(user_songs__id=user_id)


class SongDetailsView(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongDetailSerializer


class ArtistDetailsView(RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistDetailSerializer


class AlbumDetailsView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_song_to_library(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    user_songs, _ = UserSongs.objects.get_or_create(user=request.user)
    user_songs.songs.add(song)

    return Response(status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_song_from_library(request, song_id):
    song = get_object_or_404(Song, id=song_id, user_songs__user=request.user.id)
    user_songs = get_object_or_404(UserSongs, user=request.user)
    user_songs.songs.remove(song)

    return Response(status=status.HTTP_204_NO_CONTENT)
