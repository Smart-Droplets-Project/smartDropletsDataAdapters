from enum import Enum
from . import Util


class Direction(Util, Enum):
    INLET = "Inlet",
    OUTLET = "Outlet",
    ENTRY = "Entry",
    EXIT = "Exit"