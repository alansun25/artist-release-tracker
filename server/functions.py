import os
import random as rand
import spotipy
import string
from artist_radar import ArtistRadar
from init.firebase import initialize_firebase_db
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
R_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
SCOPE = os.environ.get("SPOTIPY_SCOPE")

AUTH = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, R_URI, scope=SCOPE)
TOKEN_DATA = {}

def create_secret_key(size):
    return ''.join(rand.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))

def get_auth_url():
    return AUTH.get_authorize_url()

def get_token_data(code):
    global TOKEN_DATA
    
    TOKEN_DATA = AUTH.get_cached_token()
    if not TOKEN_DATA:
        TOKEN_DATA = AUTH.get_access_token(code)
    
    initialize_spotify_client()

def refresh_token():
    # Note: Spotify access tokens have a lifetime of 1 hour
    global TOKEN_DATA
    
    if AUTH.is_token_expired(TOKEN_DATA):
        TOKEN_DATA = AUTH.refresh_access_token(TOKEN_DATA['refresh_token'])
        initialize_spotify_client()

def initialize_spotify_client():
    global sp    
    sp = spotipy.Spotify(TOKEN_DATA['access_token'])

def create_artist_radar():
    return ArtistRadar(sp, initialize_firebase_db())