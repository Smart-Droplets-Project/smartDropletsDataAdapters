import dataclasses
from typing import Optional

from ... import Util


@dataclasses.dataclass
class Destination(Util):
    geographicPoint: Optional[object] = None
    mapId: Optional[str] = None
    orientation2D: Optional[object] = None
    orientation3D: Optional[object] = None
    point2D: Optional[object] = None
    point3D: Optional[object] = None