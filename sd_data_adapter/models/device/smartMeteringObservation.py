from dataclasses import dataclass
from typing import Optional, Union

from .. import Devices, Property, GeoProperty, Relationship


@dataclass
class SmartMeteringObservation(Devices):
    """
    The `SmartMeteringObservation` class represents an observation of a smart metering device. It inherits from the `Devices` class.

    Attributes:
        address (Optional[Property]): The address of the smart metering device.
        alternateName (Optional[Property]): An alternate name for the smart metering device.
        areaServed (Optional[Property]): The area served by the smart metering device.
        dataProvider (Optional[Property]): The data provider for the smart metering device.
        dateCreated (Optional[Property]): The date when the data was created.
        dateModified (Optional[Property]): The date when the data was last modified.
        description (Optional[Property]): A description of the smart metering device.
        name (Optional[Property]): The name of the smart metering device.
        owner (Optional[Property]): The owner of the smart metering device.
        seeAlso (Optional[Property]): A URL that provides additional information about the smart metering device.
        source (Optional[Property]): The source of the data for the smart metering device.
        location (Optional[GeoProperty]): The geographic location of the smart metering device.
        entityVersion (Optional[Property]): The version of the smart metering device.
        meterType (Optional[Property]): The type of the smart metering device.
        offPeakConsumption (Optional[Property]): The off-peak consumption of the smart metering device.
        peakConsumption (Optional[Property]): The peak consumption of the smart metering device.
        powerFactor (Optional[Property]): The power factor of the smart metering device.
        refDevice (Optional[Union[Property, Relationship]]): A reference to another device related to the smart metering device.
        totalConsumption (Optional[Property]): The total consumption of the smart metering device.
        image (Optional[Union[Property, Relationship]]): An image of the smart metering device.

    """

    address: Optional[Property] = None
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
    entityVersion: Optional[Property] = None
    meterType: Optional[Property] = None
    offPeakConsumption: Optional[Property] = None
    peakConsumption: Optional[Property] = None
    powerFactor: Optional[Property] = None
    refDevice: Optional[Union[Property, Relationship]] = None
    totalConsumption: Optional[Property] = None
    image: Optional[Union[Property, Relationship]] = None