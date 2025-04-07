from dataclasses import dataclass
from typing import Optional

from .. import Property, GeoProperty, Weather


@dataclass
class SeaConditions(Weather):
    """
    Class representing sea conditions observations.

    Attributes:
        id (str): The unique identifier of the sea conditions observation.
        type (str): The type of the observation (should be "SeaConditions").

    Optional Attributes:
        address (Optional[Property]): The address associated with the observation location.
            Includes nested fields:
            - addressCountry
            - addressLocality
            - addressRegion
            - district
            - postOfficeBoxNumber
            - postalCode
            - streetAddress
            - streetNr
        alternateName (Optional[str]): An alternate name for this observation.
        areaServed (Optional[str]): The geographic area where the observation is relevant.
        dataProvider (Optional[str]): The provider of the data.
        dateCreated (Optional[str]): The date when this observation was created in the system.
        dateModified (Optional[str]): The date when this observation was last modified.
        dateObserved (Optional[str]): The date and time of the observation in ISO8601 format.
        description (Optional[str]): A description of the sea conditions.
        location (Optional[GeoProperty]): The geographic location of the observation.
            Includes:
            - coordinates (GeoJSON format)
            - bbox (bounding box)
        name (Optional[str]): The name of this observation.
        owner (Optional[List[str]]): Owners of this observation.
        pH (Optional[float]): The pH level of the seawater.
        salinity (Optional[float]): The salinity level of the seawater.
        seeAlso (Optional[List[str]]): List of URIs pointing to additional resources.
        source (Optional[List[str]]): List of sources for this observation.
        surfaceTemperature (Optional[float]): The temperature at the sea surface.
        waveHeight (Optional[float]): The height of waves.
        waveLevel (Optional[str]): The level classification of waves.
        wavePeriod (Optional[float]): The period between waves in seconds.
    """

    address: Optional[Property] = None
    alternateName: Optional[Property] = None
    areaServed: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dateCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    dateObserved: Optional[Property] = None
    description: Optional[Property] = None
    location: Optional[GeoProperty] = None
    name: Optional[Property] = None
    owner: Optional[Property] = None
    pH: Optional[Property] = None
    salinity: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
    surfaceTemperature: Optional[Property] = None
    waveHeight: Optional[Property] = None
    waveLevel: Optional[Property] = None
    wavePeriod: Optional[Property] = None