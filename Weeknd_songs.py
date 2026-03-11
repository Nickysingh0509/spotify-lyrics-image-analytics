# SONG LIST
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas

# Spotify credentials
client_id = "YOUR_SPOTIFY_CLIENT_ID"
client_secret = "YOUR_SPOTIFY_CLIENT_SECRET"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

output = {'SongName': [], "AlbumName": []}

# artist name
name = ['the weeknd']
result = sp.search(name)
result['tracks']['items'][1]['artists']

# Extract Artist's uri
artists_uris = result['tracks']['items'][0]['artists'][0]['uri']

# Pull all of the artist's albums
artist_albums = sp.artist_albums(artists_uris, album_type='album')

# Store album names and uris
artist_album_names = []
artist_album_uris = []
for i in range(len(artist_albums['items'])):
    artist_album_names.append(artist_albums['items'][i]['name'])
    artist_album_uris.append(artist_albums['items'][i]['uri'])

# Extract songs from every album
def album_songs(uri):
    album = uri
    spotify_albums[album] = {}
    spotify_albums[album]['album'] = []
    spotify_albums[album]['track_number'] = []
    spotify_albums[album]['id'] = []
    spotify_albums[album]['name'] = []
    spotify_albums[album]['uri'] = []
    tracks = sp.album_tracks(album)

    for n in range(len(tracks['items'])):
        spotify_albums[album]['album'].append(artist_album_names[album_count])
        spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
        spotify_albums[album]['id'].append(tracks['items'][n]['id'])
        spotify_albums[album]['name'].append(tracks['items'][n]['name'])
        spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])
        output['SongName'].append(tracks['items'][n]['name'])
        output['AlbumName'].append(artist_album_names[album_count])

spotify_albums = {}
album_count = 0
for i in artist_album_uris:
    album_songs(i)
    album_count += 1

results = pandas.DataFrame(output)
results.to_csv('weeknd_songs_list.csv', index=True, index_label="Index")
print("Songs list saved → weeknd_songs_list.csv")

# LYRICS
import pandas as pd
import lyricsgenius

# Read the songs we just saved
input_data_in_dataframe = pd.read_csv("weeknd_songs_list.csv")

SongNames = input_data_in_dataframe['SongName']
SongNamesList = list(SongNames)

separator = ' -'
cleanedsonglist = []
for song in SongNamesList:
    cleansong = str(song).split(separator, 1)[0]
    cleanedsonglist.append(cleansong)

# Genius token + timeout
genius = lyricsgenius.Genius('YOUR_GENIUS_API_KEY', timeout=120)


artist_name = "The Weeknd"
output_lyrics = {"Song": [], "Lyrics": [], "Artist": []}

for song_title in cleanedsonglist:
    print("Song:", song_title)
    song = genius.search_song(song_title, artist_name)
    if song is not None and song.lyrics is not None:
        cleanedlyrics = song.lyrics.split("\n", 1)[1] if "\n" in song.lyrics else song.lyrics
        output_lyrics['Song'].append(song_title)
        output_lyrics['Lyrics'].append(cleanedlyrics)
        output_lyrics['Artist'].append(artist_name)

lyrics_results = pandas.DataFrame(output_lyrics)
lyrics_results.to_csv('weeknd_lyrics.csv', index=True, index_label="Index")
print("Lyrics saved → weeknd_lyrics.csv")
