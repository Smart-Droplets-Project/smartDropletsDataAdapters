from enum import Enum

from . import Util
from dataclasses import dataclass


@dataclass
class DeviceCategory(Util, Enum):
    ACTUATOR = 'actuator'
    BEACON = 'beacon'
    END_GUN = 'endgun'
    HVAC = 'HVAC'
    IMPLEMENT = 'implement'
    IRR_SECTION = 'irrSection'
    IRR_SYSTEM = 'irrSystem'
    METER = 'meter'
    MULTIMEDIA = 'multimedia'
    NETWORK = 'network'
    SENSOR = 'sensor'
