from dataclasses import dataclass
from typing import Optional, List

from sd_data_adapter.models.agrifood.AgriProductType import AgriProductType


@dataclass
class AgriPest:
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
    id: str
    type: str
    name: str

    agroVocConcept: Optional[str] = None
    alternateName: Optional[str] = None
    dataProvider: Optional[str] = None
    dataCreated: Optional[str] = None
    dateModified: Optional[str] = None
    description: Optional[str] = None
    hasAgriProductType: Optional[List[AgriProductType | str]] = None
    owner: Optional[str] = None
    relatedSource: Optional[List[str]] = None
    seeAlso: Optional[List[str]] = None
    source: Optional[List[str]] = None