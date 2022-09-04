import json


class RadarPlaylist:
    def __init__(self, id, name, tracked_artists_ids):
        self.id = id
        self.name = name
        self.tracked_artists_ids = tracked_artists_ids

    def set(self, key, value):
        setattr(self, key, value)

    def to_dict(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

    def from_dict(dict):
        return RadarPlaylist(dict["id"], dict["name"], dict["tracked_artists_ids"])
