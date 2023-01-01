import spotipy
from datetime import datetime
from models.artist import Artist
from models.playlist_data import PlaylistData
from models.radar_playlist import RadarPlaylist
from models.track import Track

class ArtistRadar:
    def __init__(self, sp: spotipy.Spotify, db):
        self.sp = sp
        self.user = self.sp.current_user()
        self.user_playlists = self.sp.user_playlists(self.user["id"])
        
        self.tracked_artists = []
        
        self.user_doc = db.collection("users").document(self.user["id"])
        doc = self.user_doc.get()
        if doc.exists:
            self.radar_playlist = RadarPlaylist.from_dict(self.user_doc.get().to_dict())
            if not self.playlist_exists(self.radar_playlist.id):
                # If the user deleted the playlist at some point, 
                # recreate it and rewrite the old data
                self.create_radar_playlist()
            else:
                self.tracked_artists = self.radar_playlist.tracked_artists_ids
        else:
            self.radar_playlist = None
            self.create_radar_playlist()    
    
    def create_radar_playlist(self):
        name = "Spotify Artist Radar"
        count = 1
        while self.playlist_name_taken(name):
            name = f"Spotify Artist Radar {count}"
            count += 1
        desc = "Newest releases from your selected artists."
        
        self.radar_playlist = self.sp.user_playlist_create(
            self.user["id"], name, False, False, desc
        )
        
        playlist_data = RadarPlaylist(self.radar_playlist["id"], name, [])
        self.user_doc.set(playlist_data.to_dict())
    
    def search_artist(self, artist_name):
        search_results = self.sp.search(
            artist_name, 50, 0, "artist", self.user["country"]
        )["artists"]["items"]

        # Sort by artist popularity first and then total follower count (most to least).
        search_results.sort(
            key=lambda i: (i["popularity"], i["followers"]["total"]), reverse=True
        )
        
        artists = []
        for res in search_results:
            artists.append(Artist(
                res["external_urls"]["spotify"], 
                res["name"], 
                res["images"][0]["url"], 
                res["followers"]["total"],
                res["genres"]
            ).to_dict())
        
        return artists

    def get_tracked_artists_info(self):
        artist_data = []
        for artist_id in self.tracked_artists:
            artist = self.sp.artist(artist_id)
            artist_data.append(Artist(
                artist["external_urls"]["spotify"], 
                artist["name"], 
                artist["images"][0]["url"], 
                artist["followers"]["total"],
                artist["genres"]
            ).to_dict())
            
        return artist_data
    
    def get_radar_playlist_tracks(self):
        playlist = self.sp.playlist(self.radar_playlist.id)
        
        tracks = []
        for track_item in playlist["tracks"]["items"]:
            track = track_item["track"]
            
            artists = []
            for artist in track["artists"]:
                artists.append({"name": artist["name"], "url": artist["external_urls"]["spotify"]})
            
            tracks.append(Track(
                track["external_urls"]["spotify"], 
                track["name"], 
                track["album"]["name"], 
                track["album"]["external_urls"]["spotify"], 
                artists, 
                track["album"]["images"][0]["url"]
            ).to_dict())
        
        return PlaylistData(playlist["external_urls"]["spotify"], tracks).to_dict()
    
    def playlist_exists(self, playlist_id):
        for playlist in self.user_playlists["items"]:
            if playlist["id"] == playlist_id:
                return True

        return False
    
    
    ### OLD ###
    
    def create_playlist(self):
        """
        Create the user's artist radar playlist.
        """

        playlist_name = input(
            "Enter the name of your new playlist or an existing playlist (case sensitive):\n"
        )

        if self.playlist_name_taken(playlist_name):
            for playlist in self.user_playlists["items"]:
                if playlist["name"] == playlist_name:
                    radar_playlist_id = playlist["id"]
        else:
            playlist_desc = input("Enter a description for your new playlist:\n")
            playlist = self.sp.user_playlist_create(
                self.user["id"], playlist_name, False, False, playlist_desc
            )
            radar_playlist_id = playlist["id"]

        if self.user_doc.get().exists:
            user_radar_playlist = RadarPlaylist.from_dict(self.user_doc.get().to_dict())
            tracked_artists = user_radar_playlist.tracked_artists_ids
        else:
            user_radar_playlist = RadarPlaylist(radar_playlist_id, playlist_name, [])
            tracked_artists = []

        user_radar_playlist.tracked_artists_ids = self.get_tracked_artists_ids(
            tracked_artists
        )

        self.user_doc.set(
            user_radar_playlist.to_dict(),
            merge=True,
        )

        most_recent_tracks = self.get_most_recent_tracks(
            user_radar_playlist.tracked_artists_ids
        )

        # Update playlist.
        self.sp.playlist_replace_items(radar_playlist_id, most_recent_tracks)

    def playlist_name_taken(self, playlist_name):
        """
        Check whether the playlist name is taken.

        :param playlist_name: Name of the playlist
        :return: Boolean for whether the playlist exists
        """

        for playlist in self.user_playlists["items"]:
            if playlist["name"] == playlist_name:
                return True

        return False

    def get_tracked_artists_ids(self, tracked_artists):
        while True:
            # Prompt the user to provide artists for which they would like to track new releases.
            artist_name = input(
                "Name of an artist you would like to track (type 'exit' when done):\n"
            ).strip()

            if artist_name.lower() == "exit":
                break

            artist_id = self.search_artist_id_by_name(artist_name)

            # Check that the artist ID is not already in the user's list of tracked artists.
            if artist_id not in tracked_artists:
                tracked_artists.append(artist_id)

        return tracked_artists

    def search_artist_id_by_name(self, artist_name):
        search_results = self.sp.search(
            artist_name, 10, 0, "artist", self.user["country"]
        )["artists"]["items"]

        # Sort by artist popularity first and then total follower count (most to least).
        search_results.sort(
            key=lambda i: (i["popularity"], i["followers"]["total"]), reverse=True
        )

        # Select desired artist from the most popular artists retrieved (top 10 or fewer) by
        # name and genre.
        end = min(10, len(search_results))
        for i in range(0, end):
            genres = ", ".join(search_results[i]["genres"])
            if not len(genres):
                genres = "N/A"
            print(f'({i}) Artist: {search_results[i]["name"]}, Genre(s): {genres}\n')

        artist_idx = input(
            f"From the choices above, enter the index of the artist you were looking for (0 thru {end - 1}): "
        )
        artist_idx = int(artist_idx)
        while artist_idx > end - 1 or artist_idx < 0:
            artist_idx = input(f"Please enter a value between 0 and {end - 1}: ")
            artist_idx = int(artist_idx)

        artist_id = search_results[artist_idx]["id"]

        return artist_id

    def get_most_recent_tracks(self, artists_ids_list):
        most_recent_tracks = []
        for artist_id in artists_ids_list:
            # Get artist most recent release (can be a single, album, or feature).
            artist_albums = self.sp.artist_albums(
                artist_id, "album,single,appears_on", self.user["country"]
            )["items"]
            artist_albums.sort(
                key=lambda i: datetime.strptime(i["release_date"], "%Y-%m-%d"),
                reverse=True,
            )

            index = self.get_first_non_future_or_various_artists_release_index(
                artist_albums
            )

            recent_track = artist_albums[index]["id"]

            # Store new artist releases in new tracks list
            for track in self.sp.album_tracks(
                recent_track, market=self.user["country"]
            )["items"]:
                for artist in track["artists"]:
                    if artist["id"] == artist_id:
                        most_recent_tracks.append(track["id"])
                        break

        return most_recent_tracks

    def is_various_artists(self, artists):
        """
        Check whether the artists include 'Various Artists'

        :param artists: List of artists
        :return: Boolean for if 'Various Artists' is included in the artists
        """
        for artist in artists:
            if artist["name"] == "Various Artists":
                return True

        return False

    def get_first_non_future_or_various_artists_release_index(self, artist_albums):
        # Adjust for two things:
        # 1. Sometimes an artist has a release date that is in the future - ignores those.
        # 2. Ignores releases on playlists from 'Various Artists', as they are often movie/show
        #    soundtracks.
        index = 0
        artists = artist_albums[index]["artists"]
        release_date = artist_albums[index]["release_date"]
        now = datetime.now()
        while self.is_various_artists(artists) or now < datetime(
            int(release_date[0:4]), int(release_date[5:7]), int(release_date[8:])
        ):
            index += 1
            artists = artist_albums[index]["artists"]
            release_date = artist_albums[index]["release_date"]

        return index
