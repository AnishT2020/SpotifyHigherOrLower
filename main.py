import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#replace client_id and client_secret
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = '5801f1d7c9494b279259be2fe3d9aa72',
                                                                              client_secret = 'ee018dc65b4c43fbbd6827534a64747a'))

artist_uri = 'spotify:artist:5K4W6rqBFWDnAN6FQUkS6x'

results = spotify.artist_albums(artist_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
