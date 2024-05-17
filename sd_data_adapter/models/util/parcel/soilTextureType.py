from enum import Enum

from ... import Util


class SoilTextureType(Util, Enum):
    """
    Represents the different types of soil texture.

    The SoilTextureType class is an enumeration class that defines the different types of soil texture. Each type is represented by a string value.

    Attributes:
        SANDS (str): Represents sandy soil texture.
        LOAMY_SANDS (str): Represents loamy sands soil texture.
        LOAM (str): Represents loam soil texture.
        SILT_LOAM (str): Represents silt loam soil texture.
        SILT (str): Represents silt soil texture.
        SANDY_CLAY_LOAM (str): Represents sandy clay loam soil texture.
        CLAY_LOAM (str): Represents clay loam soil texture.
        SILT_CLAY_LOAM (str): Represents silt clay loam soil texture.
        SILTY_CLAY (str): Represents silty clay soil texture.
        CLAY (str): Represents clay soil texture.
    """

    SANDS = "Sands"
    LOAMY_SANDS = "Loamy sands"
    LOAM = "Loam"
    SILT_LOAM = "Silt loam"
    SILT = "Silt"
    SANDY_CLAY_LOAM = "Sandy clay loam"
    CLAY_LOAM = "Clay loam"
    SILT_CLAY_LOAM = "Silt clay loam"
    SILTY_CLAY = "Silty clay"
    CLAY = "Clay"
