from enum import Enum

from ... import Util


class OperationType(Util, Enum):
    FERTILIZER = "fertilizer"
    INSPECTION = "inspection"
    PESTICIDE = "pesticide"
    WATER = "water"
    OTHER = "other"