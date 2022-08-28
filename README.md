# Spotify Artist Radar

## Currently:
- [X] Populates a specified playlist with each specified artist's most recent single, album, or feature when you run `main.py`.
- [X] Ignores tracks from collections made by "Various Artists", i.e. movie soundtracks.
- [X] Allows the user to select from a list of artists after searching for one.
- [X] If user enters name of an artist that is already on their tracked list, don't add it again.
- [X] Make code be able to create multiple text files, one for each playlist the user creates. 
- [ ] Modularize code.
- [ ] User should input artist names for search, but I should store the artists IDs so I don't need the user to select from a list of artists each time. Right now it saves the name but the user needs to select from the list every time the script is run, which is annoying.
- [ ] Use cron jobs for repeated scheduling of the script.
- [ ] Provide a way to remove artists from tracked artist list (in the web app version eventually).

## Tools: 
- Python
- Spotify Web API
- spotipy

## Future
- Flask web app that will let anyone use this script with a simple UI.
