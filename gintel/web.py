from typing import Any

from gintel.utils import Tokens

token_cache = Tokens()


class Mapbox:
    def __init__(self, token: str | None = None) -> None:
        self.token = token

    def query(self, **kwargs) -> Any:
        pass


class Endpoint:
    def __init__(self):
        self.mapbox = Mapbox()
