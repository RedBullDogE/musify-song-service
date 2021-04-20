from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Album, Artist, Song, UserSongs
from .serializers import (
    AlbumDetailSerializer,
    AlbumListSerializer,
    ArtistDetailSerializer,
    ArtistListSerializer,
    SongDetailSerializer,
    SongListSerializer,
)


class LibraryView(ListAPIView):
    serializer_class = SongListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return Song.objects.filter(user_songs__id=user_id)


class SongReadViewSet(ReadOnlyModelViewSet):
    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return SongListSerializer
        elif self.action == "retrieve":
            return SongDetailSerializer


class ArtistReadViewSet(ReadOnlyModelViewSet):
    queryset = Artist.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ArtistListSerializer
        elif self.action == "retrieve":
            return ArtistDetailSerializer


class AlbumReadViewSet(ReadOnlyModelViewSet):
    queryset = Album.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return AlbumListSerializer
        elif self.action == "retrieve":
            return AlbumDetailSerializer


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
