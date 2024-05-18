import dataclasses
from typing import Optional

from ... import Property, Util


@dataclasses.dataclass
class Battery(Util):
    current: Optional[Property] = None
    remainingPercentage: Optional[Property] = None
    remainingTime: Optional[Property] = None
    voltage: Optional[Property] = None