from rest_framework import serializers
from myapp.models import Song, Artist, Album

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title', 'url', 'img_url']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name', 'img_url', 'description']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id','name', 'img_url', 'description']