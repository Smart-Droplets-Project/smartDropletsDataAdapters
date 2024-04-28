from enum import Enum

from sd_data_adapter.models import Util


class OperationType(Util, Enum):
    FERTILIZER = "fertilizer"
    INSPECTION = "inspection"
    PESTICIDE = "pesticide"
    WATER = "water"
    OTHER = "other"