import json

class Track:
    def __init__(self, url, name, album, album_url, artists, image):
        self.url = url
        self.name = name
        self.album = album
        self.album_url = album_url
        self.artists = artists
        self.image = image

    def to_dict(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))