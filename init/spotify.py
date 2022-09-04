import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def initialize_spotify_client():
    # Get Spotify OAuth credentials
    id = os.environ.get("SPOTIPY_CLIENT_ID")
    secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
    r_uri = os.environ.get("SPOTIPY_REDIRECT_URI")
    scope = os.environ.get("SPOTIPY_SCOPE")

    # Create Spotify API Client
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=id, client_secret=secret, redirect_uri=r_uri, scope=scope
        )
    )

    return sp
