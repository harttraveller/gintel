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
from pydantic.validators import validator


# %%
@dataclass
class Position:
    lt: float
    lg: float
    tx: int
    ty: int
    zm: int

    @validator("zm")
    def __validate_zm(cls, zm: int) -> int:
        if (zm >= 0) and (zm <= 19):
            return zm
        else:
            raise Exception("Zoom is not within allowed range: [0, 19]")

    @validator("lt")
    def __validate_lt(cls, lt: float) -> float:
        pass

    @validator("lg")
    def __validate_lg(cls, lg: float) -> float:
        pass

    @validator("tx")
    def __validate_tx(cls, tx: int) -> int:
        pass

    @validator("ty")
    def __validate_ty(cls, ty: int) -> int:
        pass

    @staticmethod
    def __validate_loc(
        tx: int | None, ty: int | None, lt: float | None, lg: float | None
    ) -> None:
        tiles_defined = all([tx is not None, ty is not None])
        coordinates_defined = all([lt is not None, lg is not None])
        if not any([tiles_defined, coordinates_defined]):
            raise Exception("Either the tiles, or coordinates must be defined.")

    @staticmethod
    def make(
        zm: int,
        tx: int | None = None,
        ty: int | None = None,
        lt: float | None = None,
        lg: float | None = None,
    ) -> Position:
        Position.__validate_zm(zm)
        Position.__validate_loc(tx, ty, lt, lg)

    @property
    def coordinates(self) -> tuple[float]:
        return (self.lt, self.lg)

    def deg2num(lat_deg, lon_deg, zoom):
        lat_rad = math.radians(lat_deg)
        n = 2.0**zoom
        xtile = int((lon_deg + 180.0) / 360.0 * n)
        ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
        return (xtile, ytile)

    def save():
        pass


# %%
pos = Position.make(zm=14, lt=100, lg=100)

# %%
