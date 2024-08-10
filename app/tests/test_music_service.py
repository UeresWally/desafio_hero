import unittest
from unittest.mock import patch
from app.services.music_service import get_playlist

class TestMusicService(unittest.TestCase):

    @patch('app.services.music_service.get_spotify_client')
    def test_get_playlist_pop(self, mock_spotify_client):
        mock_spotify_client.return_value.search.return_value = {
            'playlists': {
                'items': [
                    {'id': 'asd65fa897f'}
                ]
            }
        }

        mock_spotify_client.return_value.playlist_tracks.return_value =  {
            'items': [
                {'track': {'name': 'Umbrella'}},
                {'track': {'name': 'Tik Tok'}},
                {'track': {'name': 'I love it'}}
            ]
        }

        playlist = get_playlist(26)
        self.assertEqual(playlist, ['Umbrella', 'Tik Tok', 'I love it'])
    

    @patch('app.services.music_service.get_spotify_client')
    def test_get_playlist_rock(self, mock_spotify_client):
        mock_spotify_client.return_value.search.return_value = {
            'playlists': {
                'items': [
                    {'id': 'asd65fa897f'}
                ]
            }
        }

        mock_spotify_client.return_value.playlist_tracks.return_value =  {
            'items': [
                {'track': {'name': 'Lonely day'}},
                {'track': {'name': 'Foxy Lady'}},
                {'track': {'name': 'You give love a bad name'}}
            ]
        }

        playlist = get_playlist(15)
        self.assertEqual(playlist, ['Lonely day', 'Foxy Lady', 'You give love a bad name'])
    

    @patch('app.services.music_service.get_spotify_client')
    def test_get_playlist_classical(self, mock_spotify_client):
        mock_spotify_client.return_value.search.return_value = {
            'playlists': {
                'items': [
                    {'id': 'asd65fa897f'}
                ]
            }
        }

        mock_spotify_client.return_value.playlist_tracks.return_value =  {
            'items': [
                {'track': {'name': 'Für Elise'}},
                {'track': {'name': 'Danúbio Azul'}},
                {'track': {'name': 'Sinfonia Nº 5'}}
            ]
        }

        playlist = get_playlist(15)
        self.assertEqual(playlist, ['Für Elise', 'Danúbio Azul', 'Sinfonia Nº 5'])