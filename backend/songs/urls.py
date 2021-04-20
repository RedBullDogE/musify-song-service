from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AlbumReadViewSet,
    ArtistReadViewSet,
    LibraryView,
    SongReadViewSet,
    add_song_to_library,
    remove_song_from_library,
)

router = DefaultRouter()
router.register("songs", SongReadViewSet)
router.register("artists", ArtistReadViewSet)
router.register("albums", AlbumReadViewSet)

urlpatterns = router.urls + [
    path("lib/", LibraryView.as_view()),
    path("add-song/<int:song_id>/", add_song_to_library),
    path("remove-song/<int:song_id>/", remove_song_from_library),
]
