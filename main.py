import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import openpyxl

df = pd.read_excel(file_path)
df['Checked'] = False

# Function to check off an album
def check_off(album):
    if album in df['Album Title'].values:
        df.loc[df['Album Title'] == album, 'Checked'] = True
        print(f"Checked off {album}!")
    else:
        print(f"{album} not found in list.")

# Print the DataFrame
print(df)

client_id = 
client_secret = 
redirect_uri = 

scope = 'user-library-read user-library-modify'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
user = sp.current_user()
print(user)
for _, row in df.iterrows():
    album_title = row['Album Title']
    artist_name = row['Artist']

    # Search for the album on Spotify
    query = f"album:{album_title} artist:{artist_name}"
    results = sp.search(query, type='album', limit=1)

    # Check if the album is found
    if results['albums']['items']:
        album = results['albums']['items'][0]
        album_id = album['id']

        # Check if the album is already in the library
        if not sp.current_user_saved_albums_contains([album_id])[0]:
            # If not, save the album to the library
            sp.current_user_saved_albums_add([album_id])
            print(f"Saved {album_title} by {artist_name} to the library")
        else:
            print(f"Album already in library: {album_title} by {artist_name}")
    else:
        print(f"Album not found: {album_title} by {artist_name}")

print("Album saving complete!")
