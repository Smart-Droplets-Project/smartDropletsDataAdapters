from typing import Optional
from dataclasses import dataclass

from ... import Util
from .cameraType import CameraType
from .cameraUsage import CameraUsage
from .deviceCategory import DeviceCategory
from .direction import Direction


@dataclass
class CameraOrientation(Util):
    annotatedMap: Optional[str] = None
    comments: Optional[str] = None
