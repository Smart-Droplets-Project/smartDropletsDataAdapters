from enum import Enum

from . import Util


class RobotResult(Util, Enum):
    ACK = "ack",
    ERROR = "error",
    IGNORE = "ignore"