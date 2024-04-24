from enum import Enum


class WaterSource(Enum):
    BOREHOLE = "borehole"
    RAINFALL = "rainfall"
    RAINWATER_CAPTURE = "rainwater capture"
    WATER_DAM = "water dam"
    COMMERCIAL_SUPPLY = "commercial supply"