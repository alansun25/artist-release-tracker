# Spotify Artist Radar

## Currently:
- Populates a specified playlist with each specified artist's most recent single, album, or feature when you run `main.py`.
- Ignores tracks from collections made by "Various Artists", i.e. movie soundtracks.

## Todo:
- Output new songs added after running the script.
- Modularize the code.
- Create a simple Github pages website for the redirect URI.
- Run the script in the cloud so it doesn't need to be manually run to update the playlist.

## Bugs:
- Some artists are not found corrently due to how I identify artists based on artist name, popularity, and follower numbers (i.e. WOODZ is not the most popular artist with the word 'woodz' in his name).

## Tools: 
- Python
- Spotify Web API
- spotipy
