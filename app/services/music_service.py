import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials
from app.core.config import settings

def get_spotify_client():
    auth_manager = SpotifyClientCredentials(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET
    )

    return spotipy.Spotify(auth_manager=auth_manager)


def get_playlist(temperature: float) -> list:
    sp = get_spotify_client()
    if temperature > 25:
        genre = 'pop'
    elif 10 <= temperature <= 25:
        genre = 'rock'
    else:
        genre = 'classical'
    
    results =  sp.search(q=f'genre:{genre}', type='playlist', limit=1)
    playlist_id = results['playlists']['items'][0]['id']

    tracks = sp.playlist_tracks(playlist_id)
    track_list = [track['track']['name'] for track in tracks['items']]

    return track_list