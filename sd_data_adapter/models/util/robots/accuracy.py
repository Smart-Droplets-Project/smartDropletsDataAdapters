import dataclasses
from typing import Optional

from ... import Property, Util


@dataclasses.dataclass
class Accuracy(Util):
    covariance: Optional[Property] = None