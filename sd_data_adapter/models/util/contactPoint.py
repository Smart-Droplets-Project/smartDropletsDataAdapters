from dataclasses import dataclass
from typing import Optional, List

from sd_data_adapter.models.util import Util


@dataclass
class ContactPoint(Util):
    """
    Represents a contact point for a specific entity.

    Optional Attributes:
        areaServed (Optional[str]): The geographic area served by the contact point.
        availabilityRestriction (Optional[List[object]]): The availability restriction for the contact point.
        availableLanguage (Optional[List[str]]): The available languages for the contact point.
        contactOption (Optional[str]): The contact option for the contact point.
        contactType (Optional[str]): The type of contact point.
        email (Optional[str]): The email address of the contact point.
        faxNumber (Optional[str]): The fax number of the contact point.
        name (Optional[str]): The name of the contact point.
        productSupported (Optional[str]): The product supported by the contact point.
        telephone (Optional[str]): The telephone number of the contact point.
        url (Optional[str]): The URL of the contact point.
    """
    areaServed: Optional[str]
    availabilityRestriction: Optional[List[object]]
    availableLanguage: Optional[List[str]]
    contactOption: Optional[str]
    contactType: Optional[str]
    email: Optional[str]
    faxNumber: Optional[str]
    name: Optional[str]
    productSupported: Optional[str]
    telephone: Optional[str]
    url: Optional[str]