# Spotify Artist Radar

*This project is in active development and is subject to change.*

## Current Features
- Creates and populates a playlist with each specified artist's most recent single, album, or feature when you run `main.py`.
- Ignores tracks from collections made by "Various Artists", i.e. movie soundtracks.
- Allows the user to select from a list of artists after searching for one (first search result might not always be the artists being referred to).
- If user enters name of an artist that is already on their tracked list, don't add the name again.
- Playlist name, ID, and tracked artists stored in a Firebase database.

## Tools
- Python
- Firebase
- Spotify Web API
- spotipy
- Svelte
- TypeScript
