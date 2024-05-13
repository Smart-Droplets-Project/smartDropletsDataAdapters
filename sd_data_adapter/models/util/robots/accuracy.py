import dataclasses
from typing import Optional

from . import Util
from ... import Property


@dataclasses.dataclass
class Accuracy(Util):
    covariance: Optional[Property] = None