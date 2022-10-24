from flask import Flask, make_response, redirect, session
from func import create_state_key
import os

app = Flask(__name__)

@app.route('/authorize')
def authorize():
    client_id = os.environ.get("SPOTIPY_CLIENT_ID")
    r_uri = os.environ.get("SPOTIPY_REDIRECT_URI")
    scope = os.environ.get("SPOTIPY_SCOPE")
    
    state_key = create_state_key(15)
    session['state_key'] = state_key
    
    authorize_url = 'https://accounts.spotify.com/en/authorize?'
    params = 'response_type=code&client_id=' + client_id + '&redirect_uri=' + r_uri + '&scope=' + scope + '&state=' + state_key
    response = make_response(redirect(authorize_url + params))
    
    return response
    