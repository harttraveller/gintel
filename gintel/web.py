# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

# %%
import requests

from typing import Any
from abc import ABC, abstractmethod

# %%
from gintel.utils import Tokens

# %%
token_cache = Tokens()


# %%
class Endpoint(ABC):
    def __init__(self, name: str, token: str | None = None) -> None:
        self._init_name(name)
        self._init_token(token)

    def _init_name(self, name: str) -> None:
        if name in token_cache.services:
            self.name = name
        else:
            raise Exception(f"{name.title()} not a valid service.")

    def _init_token(self, token: str | None = None) -> None:
        if token is None:
            if self.name in token_cache.defined:
                self.token = token_cache.get(self.name)
            else:
                raise Exception(
                    f"{self.name.title()} token not passed, and not available in local cache."
                )
        else:
            self.token = token

    def _validate_token(self) -> bool:
        if not self.access:
            raise Exception("Cannot access the API, token may be invalid.")

    @abstractmethod
    def _init_endpoints(self) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def access(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def query(self, **kwargs) -> Any:
        raise NotImplementedError()



# %%
class Mapbox(Endpoint):
    def __init__(self, token: str | None = None) -> None:
        super().__init__("mapbox", token)
        self._init_endpoints()
        self._validate_token()

    def _init_endpoints(self) -> None:
        self.base: str = "https://api.mapbox.com"
        self.valid: str = f"{self.base}/tokens/v2?access_token={self.token}"

    @property
    def access(self) -> bool:
        resp = requests.get(self.valid)
        return resp.json()["code"] == "TokenValid"

    def query(self, **kwargs) -> Any:
        pass


# %%
mapbox = Mapbox()

# %%
mapbox.access


# %%

# %%
class Interface:
    def __init__(self):
        self.mapbox = Mapbox()
