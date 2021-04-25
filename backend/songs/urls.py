from django.urls import include, path

from .views import (
    AlbumDetailsView,
    ArtistDetailsView,
    LibraryView,
    SongDetailsView,
    add_song_to_library,
    remove_song_from_library,
)

urlpatterns = [
    # Library related paths
    path(route="lib/", view=LibraryView.as_view(), name="song-library"),
    path(
        route="lib/add-song/<int:song_id>/",
        view=add_song_to_library,
        name="add-song-to-library",
    ),
    path(
        route="lib/remove-song/<int:song_id>/",
        view=remove_song_from_library,
        name="remove-song-from-library",
    ),
    # Entity details related paths
    path(route="song/<int:pk>", view=SongDetailsView.as_view(), name="song-details"),
    path(
        route="album/<uuid:pk>", view=AlbumDetailsView.as_view(), name="album-details"
    ),
    path(
        route="artist/<uuid:pk>",
        view=ArtistDetailsView.as_view(),
        name="artist-details",
    ),
    # Search path
    path("search/", include("search.urls")),
]
