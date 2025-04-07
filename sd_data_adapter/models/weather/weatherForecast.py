from dataclasses import dataclass
from typing import Optional, Dict, List

from .. import Property, GeoProperty, Weather


@dataclass
class WeatherForecast(Weather):
    """
    Class representing weather forecast data.

    Attributes:
        id (str): The unique identifier of the weather forecast.
        type (str): The type of the weather forecast (should be "WeatherForecast").
        dateIssued (str): The date and time when the forecast was issued in ISO8601 format.

    Optional Attributes:
        address (Optional[Address]): The address of the forecast location.
        feelLikesTemperature (Optional[float]): The apparent temperature accounting for wind chill/heat index.
        relativeHumidity (Optional[float]): Relative humidity measurement (0-100%).
        temperature (Optional[float]): Air temperature measurement.
        atmosphericPressure (Optional[float]): Atmospheric pressure measurement.
        gustSpeed (Optional[float]): Wind gust speed measurement.
        illuminance (Optional[float]): Light level measurement.
        refPointOfInterest (Optional[str]): Reference to a point of interest associated with this forecast.
        visibility (Optional[float]): Visibility distance measurement.
        weatherType (Optional[str]): Description of weather conditions.
        windDirection (Optional[float]): Wind direction in degrees (0-360).
        windSpeed (Optional[float]): Wind speed measurement.
        alternateName (Optional[str]): An alternate name for this forecast.
        areaServed (Optional[str]): The geographic area where the forecast is relevant.
        dataProvider (Optional[str]): The provider of the data.
        dateCreated (Optional[str]): The date when this forecast was created in the system.
        dateModified (Optional[str]): The date when this forecast was last modified.
        dateRetrieved (Optional[str]): The date when this forecast was retrieved.
        dayMaximum (Optional[dict]): Daily maximum values containing:
            - feelLikesTemperature (float): Maximum apparent temperature
            - relativeHumidity (float): Maximum relative humidity
            - temperature (float): Maximum air temperature
        dayMinimum (Optional[dict]): Daily minimum values containing:
            - feelLikesTemperature (float): Minimum apparent temperature
            - relativeHumidity (float): Minimum relative humidity
            - temperature (float): Minimum air temperature
        description (Optional[str]): A description of this forecast.
        location (Optional[object]): The geographic location of the forecast.
        name (Optional[str]): The name of this forecast.
        owner (Optional[List[str]]): Owners of this forecast.
        precipitation (Optional[float]): Precipitation amount measurement.
        seeAlso (Optional[List[str]]): List of URIs pointing to additional resources.
        source (Optional[List[str]]): List of sources for this forecast.
        uVIndexMax (Optional[float]): Maximum UV index for the forecast period.
        validFrom (Optional[str]): The start time when the forecast is valid.
        validTo (Optional[str]): The end time when the forecast is valid.
        validity (Optional[str]): Description of the forecast validity period.
    """

    dateIssued: Property = None

    address: Optional[Property] = None
    feelLikesTemperature: Optional[Property] = None
    relativeHumidity: Optional[Property] = None
    temperature: Optional[Property] = None
    atmosphericPressure: Optional[Property] = None
    gustSpeed: Optional[Property] = None
    illuminance: Optional[Property] = None
    refPointOfInterest: Optional[Property] = None
    visibility: Optional[Property] = None
    weatherType: Optional[Property] = None
    windDirection: Optional[Property] = None
    windSpeed: Optional[Property] = None
    alternateName: Optional[Property] = None
    areaServed: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dateCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    dateRetrieved: Optional[Property] = None
    dayMaximum: Optional[Property] = None
    dayMinimum: Optional[Property] = None
    description: Optional[Property] = None
    location: Optional[GeoProperty] = None
    name: Optional[Property] = None
    owner: Optional[Property] = None
    precipitation: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
    uVIndexMax: Optional[Property] = None
    validFrom: Optional[Property] = None
    validTo: Optional[Property] = None
    validity: Optional[Property] = None