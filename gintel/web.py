from typing import Any

from gintel.utils import Tokens

token_cache = Tokens()


class Mapbox:
    def __init__(self, token: str | None = None) -> None:
        if token is None:
            if "mapbox" in token_cache.defined:
                self.token = token_cache.get("mapbox")
            else:
                raise Exception(
                    "Mapbox token not passed, and not available in local cache."
                )
        else:
            self.token = token

    @staticmethod
    def validate(token: str) -> bool:
        pass

    def query(self, **kwargs) -> Any:
        pass


class Endpoint:
    def __init__(self):
        self.mapbox = Mapbox()
