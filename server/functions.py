import jsonpickle
import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
R_URI = os.environ.get("SPOTIPY_REDIRECT_URI")
STATE = str(os.urandom(15))
SCOPE = os.environ.get("SPOTIPY_SCOPE")

AUTH = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, R_URI, STATE, SCOPE)

def get_auth_url():
    return AUTH.get_authorize_url()

def get_token_data(code):
    token = AUTH.get_cached_token()
    if not token:
        token = AUTH.get_access_token(code)
    
    return token

def check_token_status(token):
    # Note: Spotify access tokens have a lifetime of 1 hour
    if AUTH.is_token_expired(token):
        token = AUTH.refresh_access_token(token['refresh_token'])
        return token
    
    # Returns None if token has not expired
    return None

def get_spotify_client(access_token):
    return spotipy.Spotify(access_token)

def to_json(obj):
    return jsonpickle.encode(obj)

def to_object(json):
    return jsonpickle.decode(json)