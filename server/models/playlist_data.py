import json

class PlaylistData:
    def __init__(self, url, tracks):
        self.url = url
        self.tracks = tracks

    def to_dict(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))