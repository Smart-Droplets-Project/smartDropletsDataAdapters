from enum import Enum


class IrrigationType(Enum):
    """

    This class represents the different types of irrigation methods.

    Attributes:
        SURFACE_IRRIGATION (str): Surface irrigation method.
        LOCALIZED_IRRIGATION (str): Localized irrigation method.
        DRIP_IRRIGATION (str): Drip irrigation method.
        SPRINKLER_IRRIGATION (str): Sprinkler irrigation method.
        CENTER_PIVOT_IRRIGATION (str): Center pivot irrigation method.
        LATERAL_MOVE_IRRIGATION (str): Lateral move irrigation method.
        SUB_IRRIGATION (str): Sub-irrigation method.
        MANUAL_IRRIGATION (str): Manual irrigation method.

    """

    SURFACE_IRRIGATION = "Surface irrigation"
    LOCALIZED_IRRIGATION = "Localized irrigation"
    DRIP_IRRIGATION = "Drip irrigation"
    SPRINKLER_IRRIGATION = "Sprinkler irrigation"
    CENTER_PIVOT_IRRIGATION = "Center pivot irrigation"
    LATERAL_MOVE_IRRIGATION = "Lateral move irrigation"
    SUB_IRRIGATION = "Sub-irrigation"
    MANUAL_IRRIGATION = "Manual irrigation"