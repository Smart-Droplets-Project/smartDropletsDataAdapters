from enum import Enum


class IrrigationType(Enum):
    SURFACE_IRRIGATION = "Surface irrigation"
    LOCALIZED_IRRIGATION = "Localized irrigation"
    DRIP_IRRIGATION = "Drip irrigation"
    SPRINKLER_IRRIGATION = "Sprinkler irrigation"
    CENTER_PIVOT_IRRIGATION = "Center pivot irrigation"
    LATERAL_MOVE_IRRIGATION = "Lateral move irrigation"
    SUB_IRRIGATION = "Sub-irrigation"
    MANUAL_IRRIGATION = "Manual irrigation"