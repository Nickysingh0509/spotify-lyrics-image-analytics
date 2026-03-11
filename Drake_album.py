import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# ---- Spotify API credentials ----
client_id = "YOUR_SPOTIFY_CLIENT_ID"
client_secret = "YOUR_SPOTIFY_CLIENT_SECRET"

# ---- Authentication ----
credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials)

# ---- Choose artist ----
artist_name = ['drake']   # <- just change the artist here

# ---- Search for the artist ----
result = sp.search(artist_name)
result['tracks']['items'][1]['artists']

# ---- Extract artist URI ----
artist_uri = result['tracks']['items'][0]['artists'][0]['uri']

# ---- Retrieve all albums for the artist ----
albums_data = sp.artist_albums(artist_uri, album_type='album')

# ---- Create a dictionary to store results ----
albums_output = {"AlbumTitle": [], "AlbumCoverURL": [], "ArtistName": []}

for album in albums_data['items']:
    albums_output['AlbumTitle'].append(album['name'])
    albums_output['AlbumCoverURL'].append(album['images'][0]['url'])
    albums_output['ArtistName'].append(album['artists'][0]['name'])

# ---- Save album information to a CSV file ----
albums_df = pd.DataFrame(albums_output)
albums_df.to_csv('drake_albums.csv', index=True, index_label="Index", encoding="utf-8-sig")

print("Album data successfully saved to drake_albums.csv")
