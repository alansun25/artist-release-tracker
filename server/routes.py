import os
import spotipy
import time
from flask import Flask, redirect, request, send_from_directory, session
from functions import get_auth_url, get_token_data, to_json

app = Flask(__name__)
app.config.update(SECRET_KEY=os.urandom(24))

@app.route("/")
def root():
    # if 'access_token' not in session:
    #     return redirect('/authorize')

    # return "<p>Hello, World!</p>"    
    return send_from_directory('../client/dist', 'index.html')

@app.route('/authorize')
def authorize():
    url = get_auth_url()
    return redirect(url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    token_data = get_token_data(code, state)
    
    # TODO: Handle when token data not returned due to state conflict
    session['access_token'] = token_data['access_token']
    session['refresh_token'] = token_data['refresh_token']
    session['token_expiration'] = time.time() + token_data['expires_in']
    
    session['spotify'] = to_json(spotipy.Spotify(session['access_token']))
    
    return redirect('/')

@app.route("/<path:path>")
def assets(path):
    return send_from_directory('../client/dist', path)

if __name__ == "__main__":
    app.run(debug=True)