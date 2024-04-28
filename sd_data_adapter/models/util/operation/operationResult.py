from enum import Enum

from sd_data_adapter.models import Util


class OperationResult(Util, Enum):
    OK = 'ok'
    ABORTED = 'aborted'
    FAILED = 'failed'