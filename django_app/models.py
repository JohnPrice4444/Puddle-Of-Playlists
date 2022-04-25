from django.db import models
from django.contrib.auth.models import User




class Playlist(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists", null=True, default=None)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return f"PLAYLIST: {self.name}"


class Song(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=64)
    playlists_associated = models.ManyToManyField(Playlist, related_name="songs")

    def __str__(self):
        return f"SONG: {self.name}"


class Artwork(models.Model):
    title = models.CharField(max_length=64)
    image_url = models.ImageField(upload_to="django_app/user_images")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="artworks", null=True, default=None)
    
    def __str__(self):
        return f"ARTWORK: {self.title}"