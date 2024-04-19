from dataclasses import dataclass



@dataclass
class ContactPoint:
    """
    Represents a contact point for a person or an organization.

    Attributes:
        areaServed (str): The geographical or logical area served by this contact point.
        availabilityRestriction (list[object]): A list of restrictions that apply to the availability of this contact point.
        availableLanguage (list[str]): A list of languages supported by this contact point.
        contactOption (str): The method of contact for this contact point.
        contactType (str): The type of this contact point.
        email (str): The email address for this contact point.
        faxNumber (str): The fax number for this contact point.
        name (str): The name of this contact point.
        productSupported (str): The product or service supported by this contact point.
        telephone (str): The telephone number for this contact point.
        url (str): The URL of a web page related to this contact point.
    """

    areaServed: str
    availabilityRestriction: list[object]
    availableLanguage: list[str]
    contactOption: str
    contactType: str
    email: str
    faxNumber: str
    name: str
    productSupported: str
    telephone: str
    url: str