import json
import os
from artist_radar import ArtistRadar
from flask import Flask, redirect, request, send_from_directory, session, render_template
from functions import check_token_status, get_auth_url, get_spotify_client, get_token_data
from init.firebase import initialize_firebase_db

app = Flask(__name__)
app.config.update(SECRET_KEY=os.urandom(24))

DB = initialize_firebase_db()

@app.route("/")
def root():
    if 'token' not in session:
        return render_template('login.html')
        
    return send_from_directory('../client/dist', 'index.html')

@app.route("/<path:path>")
def assets(path):
    return send_from_directory('../client/dist', path)

@app.route('/authorize')
def authorize():
    url = get_auth_url()
    return redirect(url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')
    token_data = get_token_data(code)

    session['token'] = token_data
    session['access_token'] = token_data['access_token']
    
    return redirect('/')

@app.route('/tracked_artists', methods=['GET'])
def get_tracked_artists():
    refresh_token = check_token_status(session['token'])
    if refresh_token:
        session['token'] = refresh_token
        session['access_token'] = refresh_token['access_token']
    
    sp = get_spotify_client(session['access_token'])
    artist_radar = ArtistRadar(sp, DB)
    artists = artist_radar.get_tracked_artists_info()

    return {'artists': artists} 

@app.route('/radar_playlist_tracks', methods=['GET'])
def get_radar_playlist():
    refresh_token = check_token_status(session['token'])
    if refresh_token:
        session['token'] = refresh_token
        session['access_token'] = refresh_token['access_token']
    
    sp = get_spotify_client(session['access_token'])
    artist_radar = ArtistRadar(sp, DB)
    radar_playlist = artist_radar.get_radar_playlist_tracks()
    
    return {'radar_playlist': radar_playlist}

# @app.route('/search/<artist>')
# def get_artist_search_results(artist):
#     refresh_token = check_token_status(session['token'])
#     if refresh_token:
#         session['token'] = refresh_token

@app.route('/user', methods=['GET'])
def user():
    refresh_token = check_token_status(session['token'])
    if refresh_token:
        session['token'] = refresh_token
        session['access_token'] = refresh_token['access_token']
    
    sp = get_spotify_client(session['access_token'])
    user = sp.current_user()
    
    return {'name': user['display_name'], 'image': user["images"][0]["url"]}
    
if __name__ == "__main__":
    app.run(debug=True)