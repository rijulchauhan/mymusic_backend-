from django.contrib import admin
from .models import Song, Artist, Album, SongArtistRelation, SongAlbumRelation, AlbumArtistRelation

# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(SongArtistRelation)
admin.site.register(SongAlbumRelation)
admin.site.register(AlbumArtistRelation)

