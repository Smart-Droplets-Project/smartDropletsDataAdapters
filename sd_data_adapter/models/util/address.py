from dataclasses import dataclass
from typing import Optional, List

from sd_data_adapter.models import Util


@dataclass
class Address(Util):
    """

    This class represents an address.

    Optional Attributes:
        addressCountry (Optional[str]): The country of the address.
        addressLocality (Optional[str]): The locality of the address.
        addressRegion (Optional[str]): The region of the address.
        district (Optional[str]): The district of the address.
        postOfficeBoxNumber (Optional[str]): The post office box number of the address.
        postalCode (Optional[str]): The postal code of the address.
        streetAddress (Optional[List[str]]): The street address of the address.
        streetNr (Optional[str]): The street number of the address.

    """

    addressCountry: Optional[str] = None
    addressLocality: Optional[str] = None
    addressRegion: Optional[str] = None
    district: Optional[str] = None
    postOfficeBoxNumber: Optional[str] = None
    postalCode: Optional[str] = None
    streetAddress: Optional[List[str]] = None
    streetNr: Optional[str] = None
