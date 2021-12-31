import os
import sys
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def playlist_exists(playlist_name, user_playlists):
  for playlist in user_playlists['items']:
    if playlist['name'] == playlist_name:
      return True
  
  return False

def main():
  load_dotenv()
  
  id = os.environ.get('SPOTIPY_CLIENT_ID')
  secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
  ruri = os.environ.get('SPOTIPY_REDIRECT_URI')
  scope = os.environ.get('SPOTIPY_SCOPE')

  # Create Spotify API Client
  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id,
                                                client_secret=secret,
                                                redirect_uri=ruri,
                                                scope=scope))
  
  # Get current user's playlists
  user_id = sp.me()['id']
  user_playlists = sp.user_playlists(user_id)
  
  # Create a new playlist if a playlist with the same name doesn't already exist.
  # If the playlist already exists, ask the user if they would like to use that
  # existing playlist.
  playlist_name = input("Enter the name of your new playlist:\n")
 
  if playlist_exists(playlist_name, user_playlists):
    print('Playlist named', '"' + playlist_name + '"', 'already exists.')
    prompt = input('Would you like to use the existing playlist? (y/n): ')
    prompt = prompt.lower()
    
    if prompt == 'y':
      for playlist in user_playlists['items']:
        if playlist['name'] == playlist_name:
          playlist_id = playlist['id']
    else:
      print("Please re-run the script and try again!")
      sys.exit()
  else:
    playlist_desc = input("Enter a description for your playlist:\n")
    playlist = sp.user_playlist_create(
        user_id, playlist_name, False, False, playlist_desc)
    playlist_id = playlist['id']
  
  # Prompt the user which artists for which they would like to track new releases
  artists = []
  
  while True:
    artist = input('Name of an artist you would like to track (type "exit" when done):\n')
    
    if artist == 'exit':
      break
    
    artists.append(artist)
  
  # Remove any leading/trailing whitespace from each artist's name
  for i in range(len(artists)):
    artists[i] = artists[i].strip()
    
  '''
  TODO:
  1. Add data persistence for artists to track.
  2. Add each artist's most recent release into the playlist. If adding a track from an
     artists that already has a track in the playlist, first remove that previous track.
  '''

if __name__ == "__main__":
    main()
