from enum import Enum


class OperationType(Enum):
    FERTILIZER = "fertilizer"
    INSPECTION = "inspection"
    PESTICIDE = "pesticide"
    WATER = "water"
    OTHER = "other"