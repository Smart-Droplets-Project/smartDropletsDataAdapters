from enum import Enum

from ... import Util


class WaterSource(Util, Enum):
    BOREHOLE = "borehole"
    RAINFALL = "rainfall"
    RAINWATER_CAPTURE = "rainwater capture"
    WATER_DAM = "water dam"
    COMMERCIAL_SUPPLY = "commercial supply"