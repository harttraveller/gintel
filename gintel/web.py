from typing import Any


class Mapbox:
    def __init__(self, token: str) -> None:
        self.token = token

    def query(self, **kwargs) -> Any:
        pass


class Endpoint:
    def __init__(self):
        self.mapbox = Mapbox()
