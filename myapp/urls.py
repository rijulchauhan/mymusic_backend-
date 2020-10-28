from django.urls import path
from myapp import views

urlpatterns = [
    
    path('songs', views.get_songs),
    path('song/<int:id>', views.get_song_with_id),
    path('artists', views.get_artists),
    path('albums', views.get_albums),
    path('artist/<int:id>', views.get_artist_with_id),
    path('album/<int:id>', views.get_album_with_id),
    path('addSong', views.AddSongView.as_view()),

]