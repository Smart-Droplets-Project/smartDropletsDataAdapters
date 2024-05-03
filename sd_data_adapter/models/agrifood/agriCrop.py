from dataclasses import dataclass
from typing import Optional, Union

from sd_data_adapter.models import Property, Relationship, AgriFood


@dataclass
class AgriCrop(AgriFood):
    """
    Class: AgriCrop

    Represents an agricultural crop.

    Attributes:
        id: str - The ID of the crop. Generated value: uuid.uuid4().
        type: str - The type of the crop.
        name: str - The name of the crop.

    Optional Attributes:
        agroVocConcept: Optional[str] - Reference to the agrovoc term associated with this crop.
        alternateName: Optional[str] - An alternate name for the crop.
        dataProvider: Optional[str] - The data provider for the crop.
        dataCreated: Optional[str] - The creation date of the crop data.
        dateModified: Optional[str] - The date when the crop data was last modified.
        description: Optional[str] - A description of the crop.
        plantingFrom: Optional[List[str]] - A list of the recommended planting interval date(s) for this crop. Specified using ISO8601 repeating date intervals.
        harvestingInterval: Optional[List[str]] - A list of the recommended harvesting interval date(s) for this crop. Specified using ISO8601 repeating date intervals.
        hasAgriFertilizer: Optional[List[AgriProductType]] - Reference to the recommended types of fertilizer suitable for growing this crop.
        hasAgriPest: Optional[List[AgriPest]] - Reference to the pests associated with this crop.
        hasAgriSoil: Optional[List[AgriSoil]] - Reference to the soil associated with this crop.
        owner: Optional[List[str]] - The owner(s) of the crop.
        relatedSource: Optional[List[str]] - Related sources of information for the crop.
        seeAlso: Optional[List[str]] - Links to additional related resources for the crop.
        source: Optional[List[str]] - The source(s) of the crop.
    """

    name: Property = None

    agroVocConcept: Optional[Union[Property, Relationship]] = None
    alternateName: Optional[Property] = None
    dataProvider: Optional[Property] = None
    dataCreated: Optional[Property] = None
    dateModified: Optional[Property] = None
    description: Optional[Property] = None
    plantingFrom: Optional[Property] = None
    harvestingInterval: Optional[Property] = None
    hasAgriFertilizer: Optional[Relationship] = None  # ??
    hasAgriPest: Optional[Relationship] = None
    hasAgriSoil: Optional[Relationship] = None
    owner: Optional[Property] = None
    relatedSource: Optional[Property] = None
    seeAlso: Optional[Property] = None
    source: Optional[Property] = None
