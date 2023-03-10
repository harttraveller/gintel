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
from typing import Any
from abc import ABC, abstractmethod

# %%
from gintel.utils import Tokens

# %%
token_cache = Tokens()


# %%
class Endpoint(ABC):
    def __init__(self, name: str, token: str | None = None) -> None:
        self.__init_name(name)
        self.__init_token(token)
        self.__init_endpoints()
        self.__validate_token()

    def __init_name(self, name: str) -> None:
        if self.name in token_cache.services:
            self.name = self.name
        else:
            raise Exception(f"{name.title()} not a valid service.")

    def __init_token(self, token: str | None = None) -> None:
        if token is None:
            if self.name in token_cache.defined:
                self.token = token_cache.get(self.name)
            else:
                raise Exception(
                    f"{self.name.title()} token not passed, and not available in local cache."
                )
        else:
            self.token = token

    @abstractmethod
    def __init_endpoints(self) -> None:
        raise NotImplementedError()

    def __validate_token(self) -> bool:
        if not self.access:
            raise Exception("Cannot access the API, token may be invalid.")

    @abstractmethod
    def query(self, **kwargs) -> Any:
        raise NotImplementedError()

    @property
    @abstractmethod
    def access(self) -> bool:
        raise NotImplementedError()


# %%
class Mapbox(Endpoint):
    def __init__(self, token: str | None = None) -> None:
        super().__init__("mapbox", token)

    def __init_endpoints(self) -> None:
        pass

    def query(self, **kwargs) -> Any:
        pass


# %%
class Interface:
    def __init__(self):
        self.mapbox = Mapbox()
