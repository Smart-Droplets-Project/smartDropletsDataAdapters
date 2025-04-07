from dataclasses import dataclass
from typing import Optional, List

from .. import Property, GeoProperty, Weather


@dataclass
class WeatherObserved(Weather):
    """
    Class representing observed weather data.

    Attributes:
        id (str): The unique identifier of the weather observation.
        type (str): The type of the weather observation (should be "WeatherObserved").
        dateObserved (str): The date and time of the observation in ISO8601 format.
        location (object): The geographic location of the observation.

    Optional Attributes:
        address (Optional[Address]): The address of the observation location.
        airQualityIndex (Optional[float]): Air Quality Index (AQI) value.
        airQualityIndexForecast (Optional[float]): Forecasted Air Quality Index (AQI) value.
        airTemperatureForecast (Optional[float]): Forecasted air temperature.
        airTemperatureTSA (Optional[dict]): Time series analysis of air temperature containing:
            - averageValue (float): Average temperature value
            - instValue (float): Instantaneous temperature value
            - maxOverTime (float): Maximum temperature over time period
            - minOverTime (float): Minimum temperature over time period
        alternateName (Optional[str]): An alternate name for this observation.
        aqiMajorPollutant (Optional[str]): The major pollutant determining AQI.
        aqiMajorPollutantForecast (Optional[str]): Forecasted major pollutant determining AQI.
        areaServed (Optional[str]): The geographic area where the observation is relevant.
        atmosphericPressure (Optional[float]): Atmospheric pressure measurement.
        dataProvider (Optional[str]): The provider of the data.
        dateCreated (Optional[str]): The date when this observation was created in the system.
        dateModified (Optional[str]): The date when this observation was last modified.
        description (Optional[str]): A description of this observation.
        dewPoint (Optional[float]): Dew point temperature.
        diffuseIrradiation (Optional[float]): Diffuse solar irradiation measurement.
        directIrradiation (Optional[float]): Direct solar irradiation measurement.
    """

    dateObserved: Property = None
    location: GeoProperty = None

    address: Optional[Property] = None
    airQualityIndex: Optional[Property] = None
    airQualityIndexForecast: Optional[Property] = None
    airTemperatureForecast: Optional[Property] = None
    airTemperatureTSA: Optional[Property] = None
    alternateName: Optional[Property] = None
    aqiMajorPollutant: Optional[Property] = None
    aqiMajorPollutantForecast: Optional[Property] = None
    areaServed: Optional[Property] = None
    atmosphericPressure: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dateCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    dewPoint: Optional[Property] = None
    diffuseIrradiation: Optional[Property] = None
    directIrradiation: Optional[Property] = None