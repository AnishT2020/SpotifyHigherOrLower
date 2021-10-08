from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from pprint import pprint

if len(sys.argv) > 1:
    uri = sys.argv[1]
else:
    uri = 'spotify:artist:5K4W6rqBFWDnAN6FQUkS6x'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = '',
                                                                         client_secret = ''))
response = sp.artist_top_tracks(uri)
artist = sp.artist(uri)
pprint(response)


for track in response['tracks']:
    print(artist['name'] + ': ' + track['name'])
