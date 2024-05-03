from dataclasses import dataclass
from typing import Optional

from sd_data_adapter.models import Property, GeoProperty, Relationship, AgriFood


@dataclass
class AgriParcel(AgriFood):
    """

    Class AgriParcel

    Represents an agricultural parcel.

    Attributes:
    - id (int): The unique identifier of the parcel.
    - type (str): The type of the parcel.
    - location (object): The location of the parcel. [Note: The type of location object is not specified. Please refer to the specific implementation for details.]
    - area (int): The area of the parcel in square meters.
    - hasAgriCrop (List[AgriCrop]): The list of agricultural crops associated with the parcel.

    Optional Attributes:
    - address (Optional[Address]): The address of the parcel.
    - alternateName (Optional[str]): An alternate name for the parcel.
    - areaServed (Optional[int]): The area served by the parcel.
    - belongsTo (Optional[str]): The entity to which the parcel belongs.
    - category (Optional[List[ProductCategory]]): The category of the parcel.
    - cropStatus (Optional[CropStatus]): The status of the crops in the parcel.
    - dataProvider (Optional[str]): The provider of data for the parcel.
    - dataCreated (Optional[str]): The date when the data for the parcel was created.
    - dateModified (Optional[str]): The date when the data for the parcel was last modified.
    - description (Optional[str]): A description of the parcel.
    - hasAgriParcelChildren (Optional[List[AgriParcel]]): The list of child parcels associated with the parcel.
    - hasAgriParcelParent (Optional[str]): The parent parcel of the parcel.
    - hasAgriSoil (Optional[List[AgriSoil]]): The list of agricultural soils associated with the parcel.
    - hasAgriQualityObserved (Optional[List[object]]): The list of observed agricultural quality for the parcel. [Note: The type of object is not specified. Please refer to the specific implementation for details.]
    - hasDevices (Optional[List[object]]): The list of devices associated with the parcel. [Note: The type of object is not specified. Please refer to the specific implementation for details.]
    - irrigationSystemType (Optional[IrrigationType]): The type of irrigation system used in the parcel.
    - lastPlantedAt (Optional[str]): The date when the last planting was done in the parcel.
    - name (Optional[str]): The name of the parcel.
    - ownedBy (Optional[List[str]]): Owner of the farm.
    - owner (Optional[List[str]]): The owners of the parcel.
    - relatedSource (Optional[List[str]]): The related sources of the parcel.
    - seeAlso (Optional[List[str]]): The related resources for the parcel.
    - soilTextureType (Optional[List[SoilTextureType]]): The soil texture types present in the parcel.
    - source (Optional[List[str]]): The sources of the parcel.

    """

    location: GeoProperty = None
    area: Property = 0
    hasAgriCrop: Relationship = None

    address: Optional[Property] = None
    alternateName: Optional[Property] = None
    areaServed: Optional[Property] = None
    belongsTo: Optional[Relationship] = None
    category: Optional[Property] = None
    cropStatus: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dataCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    hasAgriParcelChildren: Optional[Relationship] = None
    hasAgriParcelParent: Optional[Relationship] = None
    hasAgriSoil: Optional[Relationship] = None
    hasAgriQualityObserved: Optional[Relationship] = None
    hasDevices: Optional[Property] = None
    irrigationSystemType: Optional[Property] = None
    lastPlantedAt: Optional[Property] = None
    name: Optional[Property] = None
    ownedBy: Optional[Relationship] = None
    owner: Optional[Property] = None
    relatedSource: Optional[Property] = None
    seeAlso: Optional[Property] = None
    soilTextureType: Optional[Property] = None
    source: Optional[Property] = None
