import uuid
from dataclasses import dataclass
from typing import Optional, List

from sd_data_adapter.models.agrifood.AgriParcel import AgriParcel
from sd_data_adapter.models.util.Address import Address
from sd_data_adapter.models.util.ContactPoint import ContactPoint
from ngsildclient import Entity


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


    type: str
    id: str = str(uuid.uuid4())

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


    def create(self):
        farm = Entity('AgriFarm', f'urn:ngsi-ld:AgriFarm:crop-{self.id}-id')

        farm.prop('type', self.type)

        if self.address is not None and len(self.address) > 0:
            farm.prop('address', self.address)
        if self.alternateName is not None:
            farm.prop('alternateName', self.alternateName)
        if self.areaServed is not None:
            farm.prop('areaServed', self.areaServed)
        if self.contactPoint is not None:
            farm.prop('contactPoint', self.contactPoint)
        if self.dataProvider is not None:
            farm.prop('dataProvider', self.dataProvider)
        if self.dateCreated is not None:
            farm.prop('dateCreated', self.dateCreated)
        if self.dateModified is not None:
            farm.prop('dateModified', self.dateModified)
        if self.description is not None:
            farm.prop('description', self.description)
        if self.hasAgriParcel is not None and len(self.hasAgriParcel) > 0:
            if "urn:ngsi-ld" in self.hasAgriParcel[0]:
                farm.rel('hasAgriParcel', self.hasAgriParcel)
            else:
                farm.prop('hasAgriParcel', self.hasAgriParcel)
        else:
            farm.prop('hasAgriParcel', [])
        if self.hasBuilding is not None and len(self.hasBuilding) > 0:
            if "urn:ngsi-ld" in self.hasBuilding[0]:
                farm.rel('hasBuilding', str(self.hasBuilding))
            else:
                farm.prop('hasBuilding', self.hasBuilding)
        if self.landLocation is not None:
            farm.prop('landLocation', self.landLocation)
        if self.location is not None:
            farm.prop('location', self.location)
        if self.ownedBy is not None:
            farm.prop('ownedBy', self.ownedBy)
        if self.relatedSource is not None:
            farm.prop('relatedSource', self.relatedSource)
        if self.source is not None:
            farm.prop('source', self.source)
        if self.seeAlso is not None:
            farm.prop('seeAlso', self.seeAlso)

        return farm