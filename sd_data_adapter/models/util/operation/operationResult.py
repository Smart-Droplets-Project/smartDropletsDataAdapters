from enum import Enum

from sd_data_adapter.models.util import Util


class OperationResult(Enum, Util):
    OK = 'ok'
    ABORTED = 'aborted'
    FAILED = 'failed'