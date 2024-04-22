from dataclasses import dataclass
from typing import Optional, List
from sd_data_adapter.models.agrifood.AgriProduct import AgriProductType


@dataclass
class AgriSoil:
    """
    Class representing an agricultural soil.

    Attributes:
        id (str): The unique identifier of the pest.
        type (str): The type of the pest.
        name (str): The name of the pest.

    Optional Attributes:
        agroVocConcept (Optional[str]): Reference to the agrovoc term associated with this pest.
        alternateName (Optional[str], default=None): Alternate name of the pest.
        dataProvider (Optional[str], default=None): The data provider of the pest.
        dataCreated (Optional[str], default=None): The date when the pest data was created.
        dateModified (Optional[str], default=None): The date when the pest data was last modified.
        description (Optional[str], default=None): Description of the pest.
        hasAgriProductType (Optional[List[AgriProductType]], default=None): List of agri product types associated with the pest.
        owner (Optional[List[str]], default=None): List of owners of the pest.
        relatedSource (Optional[List[str]], default=None): List of related sources of the pest.
        seeAlso (Optional[List[str]], default=None): List of see also references related to the pest.
        source (Optional[List[str]], default=None): List of sources of the pest.

    """

    id: str
    type: str
    name: str

    agroVocConcept = Optional[str]  #Reference to the agrovoc term associated with this item
    alternateName: Optional[str] = None
    dataProvider: Optional[str] = None
    dataCreated: Optional[str] = None
    dateModified: Optional[str] = None
    description: Optional[str] = None
    hasAgriProductType: Optional[List[AgriProductType]] = None
    owner: Optional[List[str]] = None
    relatedSource: Optional[List[str]] = None
    seeAlso: Optional[List[str]] = None
    source: Optional[List[str]] = None