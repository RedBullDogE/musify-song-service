from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Album, Artist, Song
from .serializers import (
    AlbumDetailSerializer,
    AlbumListSerializer,
    ArtistDetailSerializer,
    ArtistListSerializer,
    SongDetailSerializer,
    SongListSerializer,
)


class LibraryView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongListSerializer
    permission_classes = [IsAuthenticated]


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
