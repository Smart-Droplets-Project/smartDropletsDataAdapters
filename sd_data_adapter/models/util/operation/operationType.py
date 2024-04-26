from enum import Enum

from sd_data_adapter.models.util import Util


class OperationType(Enum, Util):
    FERTILIZER = "fertilizer"
    INSPECTION = "inspection"
    PESTICIDE = "pesticide"
    WATER = "water"
    OTHER = "other"