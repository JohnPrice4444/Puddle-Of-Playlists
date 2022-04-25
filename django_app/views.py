from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import *
from .auth_views import *


class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return super().perform_create(serializer)
    
    def get_queryset(self):
        return Playlist.objects.filter(creator=self.request.user)


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ArtworkViewSet(ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.request.method == "POST":  # if the user is making a POST request it means they're signing up 
            return (permissions.AllowAny(),)  # this lets unauthorized users make POST request i.e. sign up, login, logout
        return (permissions.IsAdminUser(),) # this makes sure that only admin users have access to CRUD users i.e. if submitting a request other than a POST request 