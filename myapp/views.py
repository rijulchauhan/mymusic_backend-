from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Song, Artist, Album, SongArtistRelation, SongAlbumRelation, AlbumArtistRelation
import json


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.serializers import SongSerializer, ArtistSerializer, AlbumSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def get_songs(request):
    try:
        songs = Song.objects.all()
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_song_with_id(request, id):
    try:
        song = Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = SongSerializer(song)
    
    SARR=SongArtistRelation.objects.filter(song_id=song.id)
    artists = makeARString(SARR)
    SALR=SongAlbumRelation.objects.filter(song_id=song.id)
    album= makeALString(SALR)
    response_data = {"artists":artists, "album": album}
    response_data.update(serializer.data)
    # response = json.dumps(response_data)
    return Response(response_data)


@api_view(['GET'])
def get_artists(request):
    try:
        artists = Artist.objects.all()
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ArtistSerializer(artists, many=True )
    return Response(serializer.data)


@api_view(['GET'])
def get_artist_with_id(request, id):

    try:
        artist = Artist.objects.get(pk=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ArtistSerializer(artist)
    SARR=SongArtistRelation.objects.filter(artist_id=artist.pk)
    songs = []
    for i in SARR:
        song= { "title": i.song_id.title, "id": i.song_id.id }
        songs.append(song)
    response_data = {"songs":songs}
    response_data.update(serializer.data)
    # response = json.dumps(response_data)
    return Response(response_data)

@api_view(['GET'])
def get_albums(request):
    
    try:
        albums = Album.objects.all()
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSerializer(albums, many=True )
    return Response(serializer.data)

# def get_album_with_id(request, id):
#     data = Album.objects.get(pk=id)
#     SARR=SongAlbumRelation.objects.filter(album_id=data.pk)
#     songs = []
#     for i in SARR:
#         song= { "title": i.song_id.title, "id": i.song_id.id }
#         songs.append(song)
        
#     response = json.dumps({"pk": data.pk, "name": data.name, "dsc": data.description ,"img_url": data.img_url,"songs": songs})
#     return HttpResponse(response, content_type="text/json")

@api_view(['GET'])
def get_album_with_id(request, id):

    try:
        album = Album.objects.get(pk=id)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSerializer(album)
    SARR=SongAlbumRelation.objects.filter(album_id=album.pk)
    songs = []
    for i in SARR:
        song= { "title": i.song_id.title, "id": i.song_id.id }
        songs.append(song)
    response_data = {"songs":songs}
    response_data.update(serializer.data)
    # response = json.dumps(response_data)
    return Response(response_data)

class AddSongView(APIView):
    http_method_names = ['post']
    permission_classes=[IsAuthenticated] 
    def post(self, request):
        data = [{'name': 'Ashutosh'}]
        return JsonResponse(data, safe=False)


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

