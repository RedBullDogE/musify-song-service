from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('songs', SongReadViewSet)
router.register('artists', ArtistReadViewSet)
router.register('albums', AlbumDetailView)

urlpatterns = router.urls

# urlpatterns = [
#     path('songs/', SongListView.as_view()),
#     path('songs/<int:pk>/', SongDetailView.as_view()),
#     path('artists/', ArtistListView.as_view()),
#     path('artists/<int:pk>/', ArtistDetailView.as_view()),
# ]
