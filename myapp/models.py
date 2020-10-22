from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    img_url = models.CharField(max_length=1000)

class Artist(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=400)

    
class Album(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=1000)
    description = models.CharField(max_length=400)
    
class SongArtistRelation(models.Model):
    song_id = models.ForeignKey(Song,on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist,on_delete=models.CASCADE)

class SongAlbumRelation(models.Model):
    song_id = models.ForeignKey(Song,on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album,on_delete=models.CASCADE)

class AlbumArtistRelation(models.Model):
    song_id = models.ForeignKey(Album,on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist,on_delete=models.CASCADE)