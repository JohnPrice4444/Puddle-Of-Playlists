from platform import platform
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password



class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ["id", "creator", "name", "description", "songs"]
        
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return super().perform_create(serializer)

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id","name", "artist", "playlists_associated"]

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ["id", "creator", "title", "image_url"]
    
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
    
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)