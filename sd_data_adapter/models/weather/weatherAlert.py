from dataclasses import dataclass
from typing import Optional, List

from .. import Property, GeoProperty, Weather


@dataclass
class WeatherAlert(Weather):
    """
    Class representing a weather alert or warning.

    Attributes:
        id (str): The unique identifier of the weather alert.
        type (str): The type of the weather alert (should be "WeatherAlert").
        alertSource (str): The source or authority issuing this alert.
        category (str): The main category of the alert (e.g., "meteorological", "marine").
        subCategory (str): The sub-category providing more specific classification.
        dateIssued (str): The date and time when the alert was issued in ISO8601 format.

    Optional Attributes:
        address (Optional[Address]): The address associated with the alert location.
        alternateName (Optional[str]): An alternate name for this alert.
        areaServed (Optional[str]): The geographic area to which this alert applies.
        data (Optional[dict]): Additional structured data about the alert.
        dataProvider (Optional[str]): The provider of the alert data.
        dateCreated (Optional[str]): The date when this alert was created in the system.
        dateModified (Optional[str]): The date when this alert was last modified.
        description (Optional[str]): A detailed description of the alert.
        location (Optional[object]): The geographic location relevant to the alert.
        name (Optional[str]): The name or title of this alert.
        owner (Optional[List[str]]): Owners or responsible parties for this alert.
        seeAlso (Optional[List[str]]): List of URIs pointing to additional resources.
        severity (Optional[str]): The severity level of the alert (e.g., "moderate", "severe").
        source (Optional[List[str]]): List of sources for this alert.
        validFrom (Optional[str]): The start time when the alert becomes active.
        validTo (Optional[str]): The end time when the alert expires.
    """

    alertSource: Property = None
    category: Property = None
    subCategory: Property = None
    dateIssued: Property = None

    address: Optional[Property] = None
    alternateName: Optional[Property] = None
    areaServed: Optional[Property] = None
    data: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dateCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    location: Optional[GeoProperty] = None
    name: Optional[Property] = None
    owner: Optional[Property] = None
    seeAlso: Optional[Property] = None
    severity: Optional[Property] = None
    source: Optional[Property] = None
    validFrom: Optional[Property] = None
    validTo: Optional[Property] = None