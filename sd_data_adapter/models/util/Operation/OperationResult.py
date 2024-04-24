from enum import Enum


class OperationResult(Enum):
    OK = 'ok'
    ABORTED = 'aborted'
    FAILED = 'failed'