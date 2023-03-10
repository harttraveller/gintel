"""
Kwargs mapping

- latitude, longitude, zoom, loc (NW, NE, SW, SE, CE)
- tile_x, tile_y, zoom
- latitude, longitude, width/height (if one, assume square, if both, assume rectangle)
- lat/long upper left, lat/long lower right
- city
- country
- address
- timestamp of image (if applicable)

features
- saving .gintel saves as compressed pickle binary

TODO:
- calc distance between two lat/long points
- assert that the box is actually a rectangle, and not some other lopsided shape
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
import mercantile
from pydantic import BaseModel, validator
from gintel.env import TTC_MAP

#%%


class Coordinate(BaseModel):
    latitude: float
    longitude: float

    @property
    def pair(self) -> tuple[float]:
        return (self.latitude, self.longitude)


class Dimensions(BaseModel):
    width: float
    height: float


class Bounds(BaseModel):
    NW: Coordinate
    NE: Coordinate
    SW: Coordinate
    SE: Coordinate
    CE: Coordinate


class Box(BaseModel):
    bounds: Bounds
    dimensions: Dimensions


class Tile(BaseModel):
    """
    A single tile position.

    Args:
        x (int): _description_
        y (int): _description_
        z (int): zoom level
    """

    x: int
    y: int
    z: int


class Position(BaseModel):
    box: Box
    tile: Tile
    dimensions: Dimensions

    @staticmethod
    def make(**kwargs) -> Position:
        pass

    def save():
        pass

    @property
    def area(self) -> float:
        # ! note that this may not be accurate, as the real area is on a curved surface
        # ! and not on a flat surface.
        # TODO: update function with appropriate math
        return self.box.dimensions.width * self.box.dimensions.height

    @property
    def ranges(self):
        pass


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
    def coordinates_to_tiles(
        latitude: float, longitude: float, zoom: int, loc: str = "NW"
    ) -> tuple[int]:
        lat_rad = math.radians(latitude)
        n = 2.0**zoom
        tile_x = int((longitude + 180.0) / 360.0 * n)
        tile_y = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
        return (tile_x, tile_y)

    @staticmethod
    def tiles_to_coordinates(
        tile_x: int, tile_y: int, zoom: int, loc: str = "NW"
    ) -> tuple[float]:
        assert (
            loc in TTC_MAP.keys()
        ), f"Invalid location, must be in {list(TTC_MAP.keys())}"
        x_add, y_add = TTC_MAP[loc]
        n = 2.0**zoom
        longitude = (tile_x + x_add) / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * (tile_y + y_add) / n)))
        latitude = math.degrees(lat_rad)
        return (latitude, longitude)

    @staticmethod
    def translate(self, loc: Coordinate | Tile, target: str):
        # TODO: add coordinate translation
        pass


# %%


class Image:
    pass


# %%


class Map:
    pass


# %%


class Data:
    pass


# %%


class Gintel:
    position: Position
    # cache: bool = False # TODO: Not yet implemented

    @staticmethod
    def make(position: Position) -> Gintel:
        pass

    def build(self, **kwargs) -> bool:
        # TODO: for complex queries requiring multiple satellite images or varying data, this may be necessary
        pass

    def visualize(**kwargs):
        pass

    def save():
        pass
