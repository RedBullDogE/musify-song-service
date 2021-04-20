from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AlbumReadViewSet, ArtistReadViewSet, LibraryView, SongReadViewSet

router = DefaultRouter()
router.register("songs", SongReadViewSet)
router.register("artists", ArtistReadViewSet)
router.register("albums", AlbumReadViewSet)

urlpatterns = router.urls + [path("lib/", LibraryView.as_view())]
