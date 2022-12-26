from flask import Flask, redirect, request, session
from functions import create_secret_key, get_auth_url, get_token_data

app = Flask(__name__)
app.config.update(SECRET_KEY=create_secret_key(15))

@app.route("/")
def home():
    if 'token_received' not in session:
        return redirect('/authorize')

    return "<p>Hello, World!</p>"    

@app.route('/authorize')
def authorize():
    url = get_auth_url()
    return redirect(url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    get_token_data(code)
    session['token_received'] = True
    
    return redirect('/')
    