from dataclasses import dataclass
from typing import Optional, List

from sd_data_adapter.models.agrifood.AgriParcel import AgriParcel
from sd_data_adapter.models.util.Address import Address
from sd_data_adapter.models.util.ContactPoint import ContactPoint


@dataclass
class AgriFarm:
    """

    The `AgriFarm` class represents a farm in the agricultural industry.

    Attributes:
        id (str): The unique identifier of the farm.
        type (str): The type or category of the farm.

    Optional Attributes:
        address (Optional[List[Address]]): Address(es) of the practitioner that are not role specific (typically home address). (Default: None)
        alternateName (Optional[str]): An alternate name for the farm. (Default: None)
        areaServed (Optional[str]): The geographic area where a service or offered item is provided. (Default: None)
        contactPoint (Optional[ContactPoint]): Parking site contact point. (Default: None)
        dataProvider (Optional[str]): The identifier of the data provider. (Default: None)
        dateCreated (Optional[str]): The date when the farm was created. (Default: None)
        dateModified (Optional[str]): The date when the farm was last modified. (Default: None)
        description (Optional[str]): A description of the farm. (Default: None)
        hasAgriParcel (Optional[List[object]]): A list of agricultural parcels associated with the farm. (Default: None)
        hasBuilding (Optional[List[object]]): A list of buildings associated with the farm. (Default: None)
        landLocation (Optional[object]): The location of the farm's land. (Default: None)
        location (Optional[object]): The general location of the farm. (Default: None)
        ownedBy (Optional[List[str]]): A list of owners of the farm. (Default: None)
        relatedSource (Optional[List[str]]): A list of IDs the current entity may have in external applications. (Default: None)
        seeAlso (Optional[List[str]]): A list of uri pointing to additional resources about the item. (Default: None)
        source (Optional[List[str]]): A list of sources used to code the producer or rule for creating the display string. (Default: None)

    """


    id: str
    type: str

    address: Optional[List[Address]] = None
    alternateName: Optional[str] = None
    areaServed: Optional[str] = None
    contactPoint: Optional[ContactPoint] = None
    dataProvider: Optional[str] = None
    dateCreated: Optional[str] = None
    dateModified: Optional[str] = None
    description: Optional[str] = None
    hasAgriParcel: Optional[List[AgriParcel | str]] = None
    hasBuilding: Optional[List[object]] = None
    landLocation: Optional[object] = None
    location: Optional[object] = None
    ownedBy: Optional[str] = None
    relatedSource: Optional[List[str]] = None
    seeAlso: Optional[List[str]] = None
    source: Optional[List[str]] = None
