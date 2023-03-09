import math
from typing import Optional
from pydantic.dataclasses import dataclass
from pydantic.validators import validator


@dataclass
class Position:
    zm: int
    tx: Optional[int] = None
    ty: Optional[int] = None
    lt: Optional[float] = None
    lg: Optional[float] = None

    @validator("zm")
    def __validate_zm(cls, zm: int) -> int:
        if (zm >= 0) and (zm <= 19):
            return zm
        else:
            raise Exception("Zoom is not within allowed range: [0, 19]")

    def __post_init__(self):
        pass

    @property
    def coordinates(self) -> tuple[float]:
        return (self.lt, self.lg)

    def deg2num(lat_deg, lon_deg, zoom):
        lat_rad = math.radians(lat_deg)
        n = 2.0**zoom
        xtile = int((lon_deg + 180.0) / 360.0 * n)
        ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
        return (xtile, ytile)
