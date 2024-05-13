from dataclasses import dataclass
from typing import Optional

from sd_data_adapter.models import Devices, Property, GeoProperty


@dataclass
class Camera(Devices):
    """Class representing a camera device.

    Attributes:
        address (Optional[Property]): The address of the camera.
        alternateName (Optional[Property]): An alternate name for the camera.
        areaServed (Optional[Property]): The area served by the camera.
        cameraName (Optional[Property]): The name of the camera.
        cameraNum (Optional[Property]): The number of the camera.
        cameraOrientation (Optional[Property]): The orientation of the camera.
        cameraType (Optional[Property]): The type of the camera.
        cameraUsage (Optional[Property]): The usage of the camera.
        dataProvider (Optional[Property]): The data provider of the camera.
        dataCreated (Optional[Property]): The date when the data was created.
        dateModified (Optional[Property]): The date when the data was modified.
        description (Optional[Property]): The description of the camera.
        endDateTime (Optional[Property]): The end date and time of the camera.
        imageSnapshot (Optional[Property]): The image snapshot of the camera.
        location (Optional[GeoProperty]): The location of the camera.
        mediaURL (Optional[Property]): The URL of the media associated with the camera.
        name (Optional[Property]): The name of the camera.
        on (Optional[Property]): The state of the camera.
        owner (Optional[Property]): The owner of the camera.
        seeAlso (Optional[Property]): Additional resources related to the camera.
        source (Optional[Property]): The source of the camera.
        startDateTime (Optional[Property]): The start date and time of the camera.
        streamName (Optional[Property]): The name of the camera stream.
        streamURL (Optional[Property]): The URL of the camera stream.
    """

    address: Optional[Property] = None
    alternateName: Optional[Property] = None
    areaServed: Optional[Property] = None
    cameraName: Optional[Property] = None
    cameraNum: Optional[Property] = None
    cameraOrientation: Optional[Property] = None
    cameraType: Optional[Property] = None
    cameraUsage: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dataCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    endDateTime: Optional[Property] = None
    imageSnapshot: Optional[Property] = None
    location: Optional[GeoProperty] = None
    mediaURL: Optional[Property] = None
    name: Optional[Property] = None
    on: Optional[Property] = None
    owner: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
    startDateTime: Optional[Property] = None
    streamName: Optional[Property] = None
    streamURL: Optional[Property] = None