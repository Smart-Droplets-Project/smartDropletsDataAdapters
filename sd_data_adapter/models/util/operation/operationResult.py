from enum import Enum

from ... import Util


class OperationResult(Util, Enum):
    OK = 'ok'
    ABORTED = 'aborted'
    FAILED = 'failed'