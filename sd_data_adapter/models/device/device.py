from dataclasses import dataclass
from typing import Optional

from sd_data_adapter.models import Devices, Property, GeoProperty


@dataclass
class Device(Devices):
    """

    The Device class represents a device with various properties and attributes.

    Attributes:
        controlledProperty (Property): The controlled property of the device.
        address (Optional[Property]): The address of the device.
        alternateName (Optional[Property]): An alternate name for the device.
        areaServed (Optional[Property]): The area served by the device.
        batteryLevel (Optional[Property]): The battery level of the device.
        category (Optional[Property]): The category of the device.
        configuration (Optional[Property]): The configuration of the device.
        controlledAsset (Optional[Property]): The controlled asset of the device.
        dataProvider (Optional[Property]): The data provider of the device.
        dataCreated (Optional[Property]): The date when the data was created.
        dateModified (Optional[Property]): The date when the device was last modified.
        description (Optional[Property]): The description of the device.
        dateFirstUsed (Optional[Property]): The date when the device was first used.
        dateInstalled (Optional[Property]): The date when the device was installed.
        dateLastCalibration (Optional[Property]): The date of last calibration of the device.
        dateLastValueReported (Optional[Property]): The date when the last value was reported by the device.
        dateManufactured (Optional[Property]): The date when the device was manufactured.
        dateObserved (Optional[Property]): The date when the device was observed.
        depth (Optional[Property]): The depth of the device.
        deviceCategory (Optional[Property]): The category of the device.
        deviceState (Optional[Property]): The state of the device.
        direction (Optional[Property]): The direction of the device.
        distance (Optional[Property]): The distance of the device.
        dstAware (Optional[Property]): The DST awareness of the device.
        firmwareVersion (Optional[Property]): The firmware version of the device.
        hardwareVersion (Optional[Property]): The hardware version of the device.
        ipAddress (Optional[Property]): The IP address of the device.
        macAddress (Optional[Property]): The MAC address of the device.
        location (Optional[GeoProperty]): The location of the device.
        mcc (Optional[Property]): The MCC (Mobile Country Code) of the device.
        mnc (Optional[Property]): The MNC (Mobile Network Code) of the device.
        name (Optional[Property]): The name of the device.
        osVersion (Optional[Property]): The operating system version of the device.
        owner (Optional[Property]): The owner of the device.
        seeAlso (Optional[Property]): The "see also" reference of the device.
        source (Optional[Property]): The source of the device.
        provider (Optional[Property]): The provider of the device.
        refDeviceModel (Optional[Property]): The reference device model of the device.
        relativePosition (Optional[Property]): The relative position of the device.
        rssi (Optional[Property]): The RSSI (Received Signal Strength Indication) of the device.
        serialNumber (Optional[Property]): The serial number of the device.
        softwareVersion (Optional[Property]): The software version of the device.
        supportedProtocol (Optional[Property]): The supported protocol of the device.
        value (Optional[Property]): The value of the device.

    """

    controlledProperty: Property = None
    address: Optional[Property] = None
    alternateName: Optional[Property] = None
    areaServed: Optional[Property] = None
    batteryLevel: Optional[Property] = None
    category: Optional[Property] = None
    configuration: Optional[Property] = None
    controlledAsset: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dataCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    dateFirstUsed: Optional[Property] = None
    dateInstalled: Optional[Property] = None
    dateLastCalibration: Optional[Property] = None
    dateLastValueReported: Optional[Property] = None
    dateManufactured: Optional[Property] = None
    dateObserved: Optional[Property] = None
    depth: Optional[Property] = None
    deviceCategory: Optional[Property] = None
    deviceState: Optional[Property] = None
    direction: Optional[Property] = None
    distance: Optional[Property] = None
    dstAware: Optional[Property] = None
    firmwareVersion: Optional[Property] = None
    hardwareVersion: Optional[Property] = None
    ipAddress: Optional[Property] = None
    macAddress: Optional[Property] = None
    location: Optional[GeoProperty] = None
    mcc: Optional[Property] = None
    mnc: Optional[Property] = None
    name: Optional[Property] = None
    osVersion: Optional[Property] = None
    owner: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
    provider: Optional[Property] = None
    refDeviceModel: Optional[Property] = None
    relativePosition: Optional[Property] = None
    rssi: Optional[Property] = None
    serialNumber: Optional[Property] = None
    softwareVersion: Optional[Property] = None
    supportedProtocol: Optional[Property] = None
    value: Optional[Property] = None