from enum import Enum

from . import Util


class CameraType(Util, Enum):
    FIXED = "FIXED",
    PTZ = "PTZ",
    DOME = "DOME",
    DAY_NIGHT = "DAY/NIGHT",
    C_MOUNT = "C-MOUNT",
    BULLET = "BULLET"