import math
from typing import Optional
from pydantic.dataclasses import dataclass


@dataclass
class Position:
    zm: int
    tx: Optional[int] = None
    ty: Optional[int] = None
    lt: Optional[float] = None
    lg: Optional[float] = None

    def __post_init__(self):
        pass

    def deg2num(lat_deg, lon_deg, zoom):
        lat_rad = math.radians(lat_deg)
        n = 2.0**zoom
        xtile = int((lon_deg + 180.0) / 360.0 * n)
        ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
        return (xtile, ytile)
