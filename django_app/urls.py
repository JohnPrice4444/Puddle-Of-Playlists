from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("playlist", PlaylistViewSet, basename="playlist")
router.register("song", SongViewSet, basename="song")
router.register("artwork", ArtworkViewSet, basename="artwork")
router.register("users", UserViewSet, basename="user")


urlpatterns = [
    path('', include(router.urls)),
    path('login/', handle_login),
    path('logout/', handle_logout),
    # path('artmaker/', handle_artmaker),
    # path('lyrics/', get_lyrics)
]
