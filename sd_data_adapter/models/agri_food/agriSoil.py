from dataclasses import dataclass
from typing import Optional, Union

from .. import Property, Relationship, AgriFood


@dataclass
class AgriSoil(AgriFood):
    """
    Class representing an agricultural soil.

    Attributes:
        id (str): The unique identifier of the soil.
        type (str): The type of the soil.
        name (str): The name of the soil.

    Optional Attributes:
        agroVocConcept (Optional[str]), default=None): Reference to the agrovoc term associated with this soil.
        alternateName (Optional[str], default=None): Alternate name of the soil.
        dataProvider (Optional[str], default=None): The data provider of the soil.
        dateCreated (Optional[str], default=None): The date when the soil data was created.
        dateModified (Optional[str], default=None): The date when the soil data was last modified.
        description (Optional[str], default=None): Description of the soil.
        hasAgriProductType (Optional[List[AgriProductType] | str], default=None): List of agri product types associated with the soil.
        owner (Optional[str], default=None): Owner of the soil.
        relatedSource (Optional[List[str]], default=None): List of related sources of the soil.
        seeAlso (Optional[List[str]], default=None): List of see also references related to the soil.
        source (Optional[List[str]], default=None): List of sources of the soil.

    """

    name: Property = None

    agroVocConcept: Optional[Union[Property, Relationship]] = None
    alternateName: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dateCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    hasAgriProductType: Optional[Relationship] = None
    owner: Optional[Property] = None
    relatedSource: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
