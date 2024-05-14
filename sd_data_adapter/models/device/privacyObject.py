from dataclasses import dataclass
from typing import Optional, Union

from sd_data_adapter.models import Devices, Property, GeoProperty, Relationship


@dataclass
class PrivacyObject(Devices):
    """
    PrivacyObject class

    This class represents a privacy object and extends the Devices class.

    Attributes:
        address (Optional[Property]): The address of the privacy object.
        alternateName (Optional[Property]): An alternate name for the privacy object.
        areaServed (Optional[Property]): The area served by the privacy object.
        dataProvider (Optional[Property]): The provider of the data.
        dataCreated (Optional[Property]): The date when the data was created.
        dateModified (Optional[Property]): The date when the data was last modified.
        description (Optional[Property]): A description of the privacy object.
        name (Optional[Property]): The name of the privacy object.
        owner (Optional[Property]): The owner of the privacy object.
        seeAlso (Optional[Property]): A reference to additional information about the privacy object.
        source (Optional[Property]): The source of the privacy object.
        location (Optional[GeoProperty]): The location of the privacy object.
        category (Optional[Property]): The category of the privacy object.
        crossborderTransfer (Optional[Property]): Indicates if the privacy object's data can be transferred across borders.
        floor (Optional[Property]): The floor where the privacy object is located.
        isIndoor (Optional[Property]): Indicates if the privacy object is indoors.
        image (Optional[Union[Property, Relationship]]): An image associated with the privacy object.
        isPersonalData (Optional[Property]): Indicates if the privacy object contains personal data.
        legitimateInterest (Optional[Property]): The legitimate interest associated with the privacy object.
        purpose (Optional[Property]): The purpose of the privacy object.
        recipientList (Optional[Property]): A list of recipients of the privacy object's data.
        refDevice (Optional[Union[Property, Relationship]]): A reference to the device related to the privacy object.
        retentionPeriod (Optional[Property]): The retention period of the privacy object's data.
        user (Optional[Property]): The user associated with the privacy object.
    """
    
    address: Optional[Property] = None
    alternateName: Optional[Property] = None
    areaServed: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dataCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    name: Optional[Property] = None
    owner: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
    location: Optional[GeoProperty] = None
    category: Optional[Property] = None
    crossborderTransfer: Optional[Property] = None
    floor: Optional[Property] = None
    isIndoor: Optional[Property] = None
    image: Optional[Union[Property, Relationship]] = None
    isPersonalData: Optional[Property] = None
    legitimateInterest: Optional[Property] = None
    purpose: Optional[Property] = None
    recipientList: Optional[Property] = None
    refDevice: Optional[Union[Property, Relationship]] = None
    retentionPeriod: Optional[Property] = None
    user: Optional[Property] = None