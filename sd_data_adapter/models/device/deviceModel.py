from dataclasses import dataclass
from typing import Optional, Union

from sd_data_adapter.models import Devices, Property, GeoProperty, Relationship


@dataclass
class DeviceModel(Devices):
    """
    A class that represents a device model.

    Attributes:
        alternateName (Optional[Property]): An optional property representing the alternate name of the device model.
        annotations (Optional[Property]): An optional property representing any annotations associated with the device model.
        brandName (Optional[Property]): An optional property representing the brand name of the device model.
        color (Optional[Property]): An optional property representing the color of the device model.
        controlledProperty (Optional[Property]): An optional property representing the controlled property of the device model.
        dataProvider (Optional[Property]): An optional property representing the data provider of the device model.
        dataCreated (Optional[Property]): An optional property representing the date the data for the device model was created.
        dateModified (Optional[Property]): An optional property representing the last modified date of the device model.
        description (Optional[Property]): An optional property representing the description of the device model.
        name (Optional[Property]): An optional property representing the name of the device model.
        owner (Optional[Property]): An optional property representing the owner of the device model.
        seeAlso (Optional[Property]): An optional property representing any related resources or information.
        source (Optional[Property]): An optional property representing the source of the device model.
        deviceCategory (Optional[Property]): An optional property representing the category of the device model.
        deviceClass (Optional[Property]): An optional property representing the class of the device model.
        documentation (Optional[Property]): An optional property representing the documentation of the device model.
        energyLimitationClass (Optional[Property]): An optional property representing the energy limitation class of the device model.
        function (Optional[Property]): An optional property representing the function of the device model.
        image (Optional[Union[Property, Relationship]]): An optional property or relationship representing the image of the device model.
        macAddress (Optional[Property]): An optional property representing the MAC address of the device model.
        manufacturerName (Optional[Property]): An optional property representing the manufacturer name of the device model.
        modelName (Optional[Property]): An optional property representing the model name of the device model.
        supportedProtocol (Optional[Property]): An optional property representing the supported protocol of the device model.
        supportedUnits (Optional[Property]): An optional property representing the supported units of the device model.
    """

    alternateName: Optional[Property] = None
    annotations: Optional[Property] = None
    brandName: Optional[Property] = None
    color: Optional[Property] = None
    controlledProperty: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dataCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    name: Optional[Property] = None
    owner: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
    deviceCategory: Optional[Property] = None
    deviceClass: Optional[Property] = None
    documentation: Optional[Property] = None
    energyLimitationClass: Optional[Property] = None
    function: Optional[Property] = None
    image: Optional[Union[Property, Relationship]] = None
    macAddress: Optional[Property] = None
    manufacturerName: Optional[Property] = None
    modelName: Optional[Property] = None
    supportedProtocol: Optional[Property] = None
    supportedUnits: Optional[Property] = None