'''
BUG:
1. Some artists are not found corrently (i.e. WOODZ is not the most popular artist with the
   word 'woodz' in his name).
'''

import os
import sys
from dotenv import load_dotenv
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def playlist_exists(playlist_name, user_playlists):
  for playlist in user_playlists['items']:
    if playlist['name'] == playlist_name:
      return True
  
  return False

def isVariousArtists(i, artist_albums):
  for artist in artist_albums[i]['artists']:
    if artist['name'] == 'Various Artists':
      return True

  return False

def main():
  load_dotenv()
  
  id = os.environ.get('SPOTIPY_CLIENT_ID')
  secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
  ruri = os.environ.get('SPOTIPY_REDIRECT_URI')
  scope = os.environ.get('SPOTIPY_SCOPE')

  # Create Spotify API Client.
  sp = spotipy.Spotify(auth_manager=
                       SpotifyOAuth(client_id=id, client_secret=secret,
                                    redirect_uri=ruri, scope=scope))
  
  # Get current user's playlists.
  user = sp.me()
  user_id = user['id']
  user_playlists = sp.user_playlists(user_id)
  
  # Create a new playlist if a playlist with the same name doesn't already exist.
  # If the playlist already exists, ask the user if they would like to use that
  # existing playlist.
  playlist_name = input("Enter the name of your new playlist or an existing playlist (case sensitive):\n")
 
  if playlist_exists(playlist_name, user_playlists):
    # print('Playlist named', '"' + playlist_name + '"', 'already exists.')
    # prompt = input('Would you like to use the existing playlist? (y/n): ')
    # prompt = prompt.lower()
    
    # if prompt == 'y':
    for playlist in user_playlists['items']:
      if playlist['name'] == playlist_name:
        playlist_id = playlist['id']
    # else:
    #   print("Please re-run the script and try again with a different playlist name.")
    #   sys.exit()
  else:
    playlist_desc = input("Enter a description for your new playlist:\n")
    playlist = sp.user_playlist_create(
        user_id, playlist_name, False, False, playlist_desc)
    playlist_id = playlist['id']
  
  # Create file to store artists user wants to track (data persistence).
  artists = open('./artists.txt', 'r+')
  existing_artists = artists.readlines()
  print(existing_artists)
  
  while True:
    # Prompt the user to provide artists for which they would like to track new releases.
    artist = input('Name of an artist you would like to track (type "exit" when done):\n')
    
    if artist == 'exit':
      break
    
    # Remove any leading/trailing whitespace from artist name before adding to the file.
    artist = artist.lower().strip()
    
    # Check that the artist is not already in the user's list of tracked artists.
    if artist not in existing_artists:
      artists.write(artist + '\n')
  
  artists.close()
  
  # Replace items currently in playlist with the most recent releases from each artist.
  new_tracks = []
  with open("artists.txt", "r") as tracked_artists:
    for tracked_artist in tracked_artists:
      query_results = sp.search(tracked_artist, 10, 0, 'artist', user['country'])['artists']['items']
      
      # This assumes the user is looking for the artist with the given name that is the
      # most popular and has the most followers.
      query_results.sort(key = lambda i: (i['popularity'], i['followers']['total']), reverse = True)
      
      # Get artist most recent release (can be a single, album, or feature).
      artist_id = query_results[0]['id']
      artist_albums = sp.artist_albums(artist_id, 'album,single,appears_on', user['country'], 50)['items']
      artist_albums.sort(key=lambda i: datetime.strptime(i['release_date'], '%Y-%m-%d'), reverse = True)
      
      # Adjust for two things:
      # 1. Sometimes an artist has a release date that is in the future
      # 2. Ignores releases on playlists from 'Various Artists', as they are often movie/show
      #    soundtracks.
      i = 0
      
      present = datetime.now()
      while isVariousArtists(i, artist_albums) or \
            present < datetime(int(artist_albums[i]['release_date'][0:4]), 
                               int(artist_albums[i]['release_date'][5:7]),
                               int(artist_albums[i]['release_date'][8:])):
        i += 1
        
      recent_release = artist_albums[i]['id']
      
      # Store new artist releases in new tracks list
      for track in sp.album_tracks(recent_release, market=user['country'])['items']:
        for artist in track['artists']:
          if artist['name'].lower().strip() == tracked_artist.lower().strip():
            new_tracks.append(track['id'])
            break
  
  # Update playlist.
  sp.playlist_replace_items(playlist_id, new_tracks)
  
  # Close the file.
  tracked_artists.close()

if __name__ == "__main__":
    main()