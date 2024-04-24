import uuid
from dataclasses import dataclass
from typing import Optional, List
from uuid import UUID

from ngsildclient import Entity, SmartDataModels, Client

from sd_data_adapter.models.agrifood.AgriPest import AgriPest
from sd_data_adapter.models.agrifood.AgriProductType import AgriProductType
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

    type: str
    name: str
    id: str = str(uuid.uuid4())

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

    def create(self):
        crop = Entity('AgriCrop', f'urn:ngsi-ld:AgriCrop:crop-{self.id}-id')

        # Definitely prop
        crop.prop('name', self.name)
        if self.agroVocConcept is not None:
            crop.prop('agroVocConcept', self.agroVocConcept)
        if self.alternateName is not None:
            crop.prop('alternateName', self.alternateName)
        if self.dataProvider is not None:
            crop.prop('dataProvider', self.dataProvider)
        if self.dataCreated is not None:
            crop.prop('dataCreated', self.dataCreated)
        if self.dateModified is not None:
            crop.prop('dateModified', self.dateModified)
        if self.description is not None:
            crop.prop('description', self.description)
        if self.owner is not None:
            crop.prop('owner', self.owner)
        if self.plantingFrom is not None and len(self.plantingFrom) > 0:
            crop.prop('plantingFrom', self.plantingFrom)
        if self.relatedSource is not None and len(self.relatedSource) > 0:
            crop.prop('relatedSource', self.relatedSource)
        if self.seeAlso is not None and len(self.seeAlso) > 0:
            crop.prop('seeAlso', self.seeAlso)
        if self.source is not None and len(self.source) > 0:
            crop.prop('source', self.source)
        if self.harvestingInterval is not None and len(self.harvestingInterval) > 0:
            crop.prop('harvestingInterval', self.harvestingInterval)

        if self.hasAgriFertilizer is not None and len(self.hasAgriFertilizer) > 0:
            if "urn:ngsi-ld" in self.hasAgriFertilizer[0]:
                crop.rel('hasAgriFertilizer', self.hasAgriFertilizer)
            else:
                crop.prop('hasAgriFertilizer', self.hasAgriFertilizer)
        else:
            crop.prop('hasAgriFertilizer', [])
        if self.hasAgriPest is not None and len(self.hasAgriPest) > 0:
            if "urn:ngsi-ld" in self.hasAgriPest[0]:
                crop.rel('hasAgriPest', self.hasAgriFertilizer)
            else:
                crop.prop('hasAgriPest', self.hasAgriFertilizer)
        else:
            crop.prop('hasAgriPest', [])
        if self.hasAgriSoil is not None and len(self.hasAgriSoil) > 0:
            if "urn:ngsi-ld" in self.hasAgriSoil[0]:
                crop.rel('hasAgriSoil', self.hasAgriFertilizer)
            else:
                crop.prop('hasAgriSoil', self.hasAgriFertilizer)
        else:
            crop.prop('hasAgriSoil', [])

        return crop
