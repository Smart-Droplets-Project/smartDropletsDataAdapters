from dataclasses import dataclass
from typing import Optional, Union

from sd_data_adapter.models import Property, Relationship, AgriFood


@dataclass
class AgriPest(AgriFood):
    """
    Class representing an agricultural pest.

    Attributes:
        id (str): The unique identifier of the pest.
        type (str): The type of the pest.
        name (str): The name of the pest.

    Optional Attributes:
        agroVocConcept (Optional[str], default=None): Reference to the agrovoc term associated with this pest.
        alternateName (Optional[str], default=None): Alternate name of the pest.
        dataProvider (Optional[str], default=None): The data provider of the pest.
        dataCreated (Optional[str], default=None): The date when the pest data was created.
        dateModified (Optional[str], default=None): The date when the pest data was last modified.
        description (Optional[str], default=None): Description of the pest.
        hasAgriProductType (Optional[List[AgriProductType]], default=None): List of agri product types associated with the pest.
        owner (Optional[str], default=None): Owners of the pest.
        relatedSource (Optional[List[str]], default=None): List of related sources of the pest.
        seeAlso (Optional[List[str]], default=None): List of see also references related to the pest.
        source (Optional[List[str]], default=None): List of sources of the pest.

    """
    name: Property = None
    type: Property = 'AgriPest'

    agroVocConcept: Optional[Union[Property, Relationship]] = None
    alternateName: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dataCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    hasAgriProductType: Optional[Relationship] = None
    owner: Optional[Property] = None
    relatedSource: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
