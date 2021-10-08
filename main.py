from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys

if len(sys.argv) > 1:
    uri = sys.argv[1]
else:
    uri = 'spotify:artist:5K4W6rqBFWDnAN6FQUkS6x'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = '5801f1d7c9494b279259be2fe3d9aa72',
                                                                         client_secret = 'ee018dc65b4c43fbbd6827534a64747a'))
response = sp.artist_top_tracks(uri)

for track in response['tracks']:
    print(track['name'])
