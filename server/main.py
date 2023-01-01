from dotenv import load_dotenv
from init.spotify import initialize_spotify_client
from init.firebase import initialize_firebase_db
from artist_radar import ArtistRadar

# Script-only version
def main():
    load_dotenv()

    sp = initialize_spotify_client()
    db = initialize_firebase_db()

    artist_radar = ArtistRadar(sp, db)
    artist_radar.create_playlist()


if __name__ == "__main__":
    main()
