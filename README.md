# Spotify Artist Radar

## Currently:
- Populates a specified playlist with each specified artist's most recent single, album, or feature when you run `main.py`.
- Ignores tracks from collections made by "Various Artists", i.e. movie soundtracks.
- Requires user to have a Spotify Client ID, Client Secret, Redirect URI, and defined scope (environment variables).

## Todo:
- Allow users to use this without needing Client ID, Secret, etc. (figure out authorization flow).
- Output new songs added after running the script.
- Modularize (?) the code.
- Run the script in the cloud so it doesn't need to be manually run to update the playlist.

## Bugs:
- Some artists are not found corrently due to how I identify artists based on artist name, popularity, and follower numbers (i.e. WOODZ is not the most popular artist with the word 'woodz' in his name).

## Tools: 
- Python
- Spotify Web API
- spotipy
