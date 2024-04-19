from dataclasses import dataclass


@dataclass
class Address:
    """

        Address class represents a physical address.

        Attributes:
            addressCountry (str): The country of the address.
            addressLocality (str): The locality of the address.
            addressRegion (str): The region or province of the address.
            district (str): The district of the address.
            postOfficeBoxNumber (str): The post office box number of the address.
            postalCode (str): The postal code of the address.
            streetAddress (list[str]): List of street names in the address.
            streetNr (str): The street number of the address.

    """

    addressCountry: str
    addressLocality: str
    addressRegion: str
    district: str
    postOfficeBoxNumber: str
    postalCode: str
    streetAddress: list[str]
    streetNr: str
