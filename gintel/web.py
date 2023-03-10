class Mapbox:
    def __init__(self, token: str) -> None:
        self.token = token


class Endpoint:
    def __init__(self):
        self.mapbox = Mapbox()
