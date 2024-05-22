from dataclasses import dataclass
from typing import Optional, Union

from .. import Devices, Property, GeoProperty, Relationship


@dataclass
class DeviceOperation(Devices):
    """
    A class representing a device operation.

    Attributes:
        address (Optional[Property]): The address of the operation.
        addressedAt (Optional[Property]): The timestamp when the operation was addressed.
        alternateName (Optional[Property]): An alternate name for the operation.
        areaServed (Optional[Property]): The area served by the operation.
        dataProvider (Optional[Property]): The provider of the operation's data.
        dateCreated (Optional[Property]): The timestamp when the operation's data was created.
        dateModified (Optional[Property]): The timestamp when the operation was last modified.
        description (Optional[Property]): The description of the operation.
        name (Optional[Property]): The name of the operation.
        owner (Optional[Property]): The owner of the operation.
        seeAlso (Optional[Property]): An external resource related to the operation.
        source (Optional[Property]): The source of the operation.
        location (Optional[GeoProperty]): The location of the operation.
        device (Optional[Relationship]): The device associated with the operation.
        endedAt (Optional[Property]): The timestamp when the operation ended.
        operationType (Optional[Property]): The type of the operation.
        operator (Optional[Relationship]): The operator of the operation.
        plannedEndAt (Optional[Property]): The planned ending timestamp of the operation.
        plannedStartAt (Optional[Property]): The planned starting timestamp of the operation.
        reportedAt (Optional[Property]): The timestamp when the operation was reported.
        result (Optional[Property]): The result of the operation.
        startedAt (Optional[Property]): The timestamp when the operation started.
        status (Optional[Property]): The status of the operation.

    """

    address: Optional[Property] = None
    addressedAt: Optional[Property] = None
    alternateName: Optional[Property] = None
    areaServed: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dateCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    name: Optional[Property] = None
    owner: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
    location: Optional[GeoProperty] = None
    device: Optional[Relationship] = None
    endedAt: Optional[Property] = None
    operationType: Optional[Property] = None
    operator: Optional[Relationship] = None
    plannedEndAt: Optional[Property] = None
    plannedStartAt: Optional[Property] = None
    reportedAt: Optional[Property] = None
    result: Optional[Property] = None
    startedAt: Optional[Property] = None
    status: Optional[Property] = None
