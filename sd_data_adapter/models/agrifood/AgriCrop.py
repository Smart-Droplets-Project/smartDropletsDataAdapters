from dataclasses import dataclass
from typing import Optional, List

from sd_data_adapter.models.agrifood.AgriPest import AgriPest
from sd_data_adapter.models.agrifood.AgriProduct import AgriProductType
from sd_data_adapter.models.agrifood.AgriSoil import AgriSoil


@dataclass
class AgriCrop:
    """
    Class: AgriCrop

    Represents an agricultural crop.

    Attributes:
        id: str - The ID of the crop.
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

    id: str
    type: str
    name: str

    agroVocConcept: Optional[str] = None
    alternateName: Optional[str] = None
    dataProvider: Optional[str] = None
    dataCreated: Optional[str] = None
    dateModified: Optional[str] = None
    description: Optional[str] = None
    plantingFrom: Optional[List[str]] = None
    harvestingInterval: Optional[List[str]] = None
    hasAgriFertilizer: Optional[List[AgriProductType | str]] = None  #??
    hasAgriPest: Optional[List[AgriPest | str]] = None
    hasAgriSoil: Optional[List[AgriSoil | str]] = None
    owner: Optional[str] = None
    relatedSource: Optional[List[str]] = None
    seeAlso: Optional[List[str]] = None
    source: Optional[List[str]] = None
