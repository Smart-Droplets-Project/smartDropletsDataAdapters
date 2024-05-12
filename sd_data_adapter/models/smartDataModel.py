import dataclasses
import uuid
from types import NoneType
from typing import Union, List, Optional

from geojson import LineString, Point, Polygon, MultiPoint, MultiLineString, MultiPolygon
from ngsildclient import Entity


@dataclasses.dataclass
class SmartDataModel:
    id: Optional[Union[str, uuid.UUID]] = uuid.uuid4()
    type: str = "SmartDataModel"

    def __post_init__(self):
        self.type = self.__class__.__name__
        if isinstance(self.id, uuid.UUID):
            self.id = f"urn:ngsi-ld:{self.type}:{self.id}-id"


@dataclasses.dataclass
class AgriFood(SmartDataModel):
    ctx: str = "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"


class Util:
    pass


Property = Union[bool, int, float, str, List[str], SmartDataModel, List[SmartDataModel], List[Util], NoneType]
Relationship = Union[str, List[str]]
GeoProperty = Union[Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon]


def to_ngsi_ld(obj: SmartDataModel):
    entity = Entity(obj.type, obj.id)
    entity.context = obj.ctx
    for field in dataclasses.fields(obj):
        field_value = getattr(obj, field.name)
        if field_value is None or field.name == "id" or field.name == "type":
            continue

        if field.type == Property:
            entity.prop(field.name, field_value)
        elif field.type == Relationship:
            entity.rel(field.name, field_value)
        elif field.type == GeoProperty:
            entity.gprop(field.name, field_value)

    return entity


def to_object(entity: Entity):
    import sd_data_adapter.models.agrifood as models

    class_name = entity.type.split("/")[-1]
    model_class = getattr(models, class_name)
    model = model_class()
    entity_dict = entity.to_dict()
    for key in entity_dict:
        new_key = key.split("/")[-1]
        try:
            try:
                setattr(model, new_key, entity_dict[key]["value"])
            except:
                setattr(model, new_key, entity_dict[key])
        except:
            continue

    return model
