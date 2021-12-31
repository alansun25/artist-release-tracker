import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

id = os.environ.get('SPOTIPY_CLIENT_ID')
secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
ruri = os.environ.get('SPOTIPY_REDIRECT_URI')
scope = os.environ.get('SPOTIPY_SCOPE')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id,
                                               client_secret=secret,
                                               redirect_uri=ruri,
                                               scope=scope))
