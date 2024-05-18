from dataclasses import dataclass
from typing import Optional

from .. import Devices, Property, GeoProperty, Relationship


@dataclass
class DeviceMeasurement(Devices):
    """

    Class for representing a device measurement.

    Attributes:
        address (Optional[Property]): The address of the device measurement.
        alternateName (Optional[Property]): An alternate name for the device measurement.
        areaServed (Optional[Property]): The area served by the device measurement.
        controlledProperty (Optional[Property]): The controlled property of the device measurement.
        dataProvider (Optional[Property]): The data provider of the device measurement.
        dataCreated (Optional[Property]): The date when the data was created.
        dateModified (Optional[Property]): The date when the data was last modified.
        dateObserved (Optional[Property]): The date when the measurement was observed.
        description (Optional[Property]): A description of the measurement.
        name (Optional[Property]): The name of the device measurement.
        owner (Optional[Property]): The owner of the device measurement.
        seeAlso (Optional[Property]): A reference to related information.
        source (Optional[Property]): The source of the measurement data.
        deviceType (Optional[Property]): The type of the device.
        location (Optional[GeoProperty]): The location of the device measurement.
        measurementType (Optional[Property]): The type of the measurement.
        numValue (Optional[Property]): The numeric value of the measurement.
        outlier (Optional[Property]): An indicator if the measurement is an outlier.
        refDevice (Optional[Relationship]): A reference to another device.
        textValue (Optional[Property]): The text value of the measurement.
        unit (Optional[Property]): The unit of measurement.

    """

    address: Optional[Property] = None
    alternateName: Optional[Property] = None
    areaServed: Optional[Property] = None
    controlledProperty: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dataCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    dateObserved: Optional[Property] = None
    description: Optional[Property] = None
    name: Optional[Property] = None
    owner: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
    deviceType: Optional[Property] = None
    location: Optional[GeoProperty] = None
    measurementType: Optional[Property] = None
    numValue: Optional[Property] = None
    outlier: Optional[Property] = None
    refDevice: Optional[Relationship] = None
    textValue: Optional[Property] = None
    unit: Optional[Property] = None
