from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Song, Artist, Album
from .serializers import *


class SongReadViewSet(ReadOnlyModelViewSet):
    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return SongListSerializer
        elif self.action == 'retrieve':
            return SongDetailSerializer


class ArtistReadViewSet(ReadOnlyModelViewSet):
    queryset = Artist.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ArtistListSerializer
        elif self.action == 'retrieve':
            return ArtistDetailSerializer


# APIView implementation

# class SongListView(ListAPIView):
#     """
#     Display all songs with short info
#     """
#     queryset = Song.objects.all()
#     serializer_class = SongListSerializer


# class SongDetailView(RetrieveAPIView):
#     """
#     Detailed info of specific song
#     """
#     queryset = Song.objects.all()
#     serializer_class = SongDetailSerializer


# class ArtistListView(ListAPIView):
#     """
#     Display all artists
#     """
#     queryset = Artist.objects.all()
#     serializer_class = ArtistListSerializer


# class ArtistDetailView(RetrieveAPIView):
#     """
#     Artist Details
#     """
#     queryset = Artist.objects.all()
#     serializer_class = ArtistDetailSerializer


# class AlbumListView(ListAPIView):
#     """
#     Display all albums
#     """

#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer
