from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Song, Artist, Album, SongArtistRelation, SongAlbumRelation, AlbumArtistRelation
import json

# Create your views here.
def get_songs(request):
    
    response = serializers.serialize('json', Song.objects.all()[:20])
    return HttpResponse(response, content_type='text/json')



def get_song_with_id(request, id):
    data = Song.objects.get(pk=id)
    SARR=SongArtistRelation.objects.filter(song_id=data.pk)
    artists = makeARString(SARR)
    SALR=SongAlbumRelation.objects.filter(song_id=data.pk)
    album= makeALString(SALR)
        
    response = json.dumps({"pk": data.pk, "title": data.title, "img_url": data.img_url, "url": data.url,"artists":artists, "album": album})
    return HttpResponse(response, content_type="text/json")

def get_artists(request):
    
    response = serializers.serialize('json', Artist.objects.all()[:20])
    return HttpResponse(response, content_type='text/json')


def get_artist_with_id(request, id):
    data = Artist.objects.get(pk=id)
    SARR=SongArtistRelation.objects.filter(artist_id=data.pk)
    songs = []
    for i in SARR:
        song= { "title": i.song_id.title, "id": i.song_id.id }
        songs.append(song)
        
    print(songs)
    response = json.dumps({"pk": data.pk, "name": data.name,"dsc": data.description, "img_url": data.img_url,"songs": songs})
    return HttpResponse(response, content_type="text/json")


def get_albums(request):
    
    response = serializers.serialize('json', Album.objects.all()[:20])
    return HttpResponse(response, content_type='text/json')

def get_album_with_id(request, id):
    data = Album.objects.get(pk=id)
    SARR=SongAlbumRelation.objects.filter(album_id=data.pk)
    songs = []
    for i in SARR:
        song= { "title": i.song_id.title, "id": i.song_id.id }
        songs.append(song)
        
    response = json.dumps({"pk": data.pk, "name": data.name, "dsc": data.description ,"img_url": data.img_url,"songs": songs})
    return HttpResponse(response, content_type="text/json")






## Utility Functions


def makeARString(rel):
    string=str()
    a = 0
    for i in rel:
        if(a != 0):
            string +=', '
        a+=1
        string+=i.artist_id.name
    return string

def makeALString(rel):
    string=str()
    a = 0
    for i in rel:
        if(a != 0):
            string +=', '
        a+=1
        string+=i.album_id.name
    return string

