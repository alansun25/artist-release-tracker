from dotenv import load_dotenv
from spotify import initialize_spotify_client
from firebase import initialize_firebase_db
from artist_radar import ArtistRadar

def main():
  load_dotenv()

  sp = initialize_spotify_client()
  db = initialize_firebase_db()
  
  artist_radar = ArtistRadar(sp, db)
  artist_radar.create_playlist()

if __name__ == '__main__':
    main()
