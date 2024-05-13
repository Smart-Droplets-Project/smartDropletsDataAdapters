from enum import Enum

from . import Util


class CameraUsage(Util, Enum):
    SURVEILLANCE = "SURVEILLANCE",
    RLVD = "RLVD",
    ANPR_LPR = "ANPR/LPR",
    TRAFFIC = "TRAFFIC"