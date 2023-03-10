"""
Kwargs mapping

- latitude, longitude, zoom
- tile_x, tile_y, zoom
- latitude, longitude, radius (degrees, miles, kilometers)
- lat/long upper left, lat/long lower right
- city
- country
- address
- timestamp of image (if applicable)

features
- saving .gintel saves as compressed pickle binary
"""

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
from __future__ import annotations
import math
from pydantic.dataclasses import dataclass


#%%
class PositionBuilder:
    @staticmethod
    def validate_zoom(zoom: int) -> None:
        if (zoom >= 0) and (zoom <= 19):
            return zoom
        else:
            raise Exception("Zoom is not within allowed range: [0, 19]")

    @staticmethod
    def validate_latitude(latitude: float) -> float:
        if (latitude >= -90) and (latitude <= 90):
            return latitude
        else:
            raise Exception("Latitude is not within allowed range: [-90, 90]")

    @staticmethod
    def validate_longitude(longitude: float) -> float:
        if (longitude >= -180) and (longitude <= 180):
            return longitude
        else:
            raise Exception("Longitude is not within allowed range: [-180, 180]")

    @staticmethod
    def validate_tile_x(tile_x: int) -> int:
        pass

    @staticmethod
    def validate_tile_y(tile_y: int) -> int:
        pass

    @staticmethod
    def validate_location_params_filled(
        latitude: float | None,
        longitude: float | None,
        tile_x: int | None,
        tile_y: int | None,
    ) -> None:
        tiles_defined = all([tile_x is not None, tile_y is not None])
        coordinates_defined = all([latitude is not None, longitude is not None])
        if not any([tiles_defined, coordinates_defined]):
            raise Exception("Either the tiles, or coordinates must be defined.")

    @staticmethod
    def coordinates_to_tiles(latitude: float, longitude: float, zoom: int) -> tuple[int]:
        lat_rad = math.radians(latitude)
        n = 2.0**zoom
        tile_x = int((longitude + 180.0) / 360.0 * n)
        tile_y = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
        return (tile_x, tile_y)

    @staticmethod
    def tiles_to_coordinates(tile_x: int, tile_y: int, zoom: int) -> tuple[float]:
        n = 2.0**zoom
        longitude = tile_x / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * tile_y / n)))
        latitude = math.degrees(lat_rad)
        return (latitude, longitude)


# %%
@dataclass
class Position:
    latitude: float
    longitude: float
    tile_x: int
    tile_y: int
    zoom: int

    @staticmethod
    def make(**kwargs) -> Position:
        pass

    @property
    def coordinates(self) -> tuple[float]:
        return (self.latitude, self.longitude)

    def save():
        pass


# %%
@dataclass
class Image:
    pass


# %%
@dataclass
class Map:
    pass


# %%
@dataclass
class Data:
    pass


# %%
@dataclass
class Gintel:
    position: Position

    def make(**kwargs) -> Gintel:
        pass

    def visualize(**kwargs) -> Gintel:
        pass

    def save():
        pass
