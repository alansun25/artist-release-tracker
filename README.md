# Spotify Artist Radar

## Currently:
- Populates a specified playlist with each specified artist's most recent single, album, or feature when you run `main.py`.
- Ignores tracks from collections made by "Various Artists", i.e. movie soundtracks.

## Todo:
- [X] Allow the user to select from a list of artists after searching for one.
- [ ] Make description auto-update with date of most recent update.
- [X] If user enters name of an artist that is already on their tracked list, don't add it again.
- [X] Make code be able to create multiple text files, one for each playlist the user creates. 
- [ ] Create a simple Github pages website for the redirect URI.
- [ ] Run the script in the cloud so it doesn't need to be manually run to update the playlist.
- [ ] Provide a way to remove artists from tracked artist list (in the web app version eventually).

## Tools: 
- Python
- Spotify Web API
- spotipy

## Future
- Flask web app that will let anyone use this script with a simple UI.