# Spotify Artist Radar

*This project is in active development and subject to change.*

## Current Features
- Creates and populates a playlist with each specified artist's most recent single, album, or feature when you run `main.py` (in the `server` folder).
- Ignores tracks from collections made by "Various Artists", i.e. movie soundtracks.
- Allows the user to select from a list of artists after searching for one (first search result might not always be the artists being referred to).
- If user enters name of an artist that is already on their tracked list, don't add the name again.
- Playlist name, ID, and tracked artists stored in a Firebase database.

## Learnings
- How to build an API and server with Flask, and serve a Svelte client on it.
- Working with access tokens and refresh tokens in OAuth2.
- Making my server read and write data from a Firebase DB.
- It's fun and rewarding to build something for personal use.

## Tools
- Python
- Flask
- Firebase
- Svelte
