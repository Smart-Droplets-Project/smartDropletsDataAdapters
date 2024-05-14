from typing import Optional

from sd_data_adapter.models import Util
from dataclasses import dataclass
from .cameraType import CameraType


@dataclass
class CameraOrientation(Util):
    annotatedMap: Optional[str] = None
    comments: Optional[str] = None
