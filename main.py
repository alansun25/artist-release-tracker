import os
import sys
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def main():
  load_dotenv()

  id = os.environ.get('SPOTIPY_CLIENT_ID')
  secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
  ruri = os.environ.get('SPOTIPY_REDIRECT_URI')
  scope = os.environ.get('SPOTIPY_SCOPE')

  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id,
                                                client_secret=secret,
                                                redirect_uri=ruri,
                                                scope=scope))
  
  user_id = sp.me()['id']
  user_playlists = sp.user_playlists(user_id)
  
  playlist_name = input("Enter the name of your new playlist:\n")
  
  for playlist in user_playlists:
    if playlist['name'] == playlist_name:
      print('Playlist named', playlist_name, 'already exists.')
      sys.exit()
  
  # playlist = sp.user_playlist_create(user_id, "Test", False, False, "Testing my Python script")
  # playlist_id = playlist['id']

if __name__ == "__main__":
    main()
