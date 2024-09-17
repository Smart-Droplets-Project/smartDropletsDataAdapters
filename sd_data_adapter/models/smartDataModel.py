import dataclasses
import uuid
# from types import NoneType
from typing import Union, List, Optional

from geojson import LineString, Point, Polygon, MultiPoint, MultiLineString, MultiPolygon, Feature, FeatureCollection
from ngsildclient import Entity


@dataclasses.dataclass
class SmartDataModel:
    id: Optional[Union[str, uuid.UUID]] = None
    type: str = "SmartDataModel"

    def __post_init__(self):
        self.type = self.__class__.__name__
        
        if self.id is None:
            self.id = uuid.uuid4()
        
        if isinstance(self.id, uuid.UUID):
            self.id = f"urn:ngsi-ld:{self.type}:{self.id}-id"


@dataclasses.dataclass
class AgriFood(SmartDataModel):
    ctx: str = "https://raw.githubusercontent.com/smart-data-models/dataModel.Agrifood/master/context.jsonld"


@dataclasses.dataclass
class Devices(SmartDataModel):
    ctx: str = "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"


@dataclasses.dataclass
class AutonomousMobileRobot(SmartDataModel):
    ctx: str = "https://raw.githubusercontent.com/smart-data-models/dataModel.AutonomousMobileRobot/master/context.jsonld"


class Util:
    pass


Property = Union[bool, int, float, str, List[str], SmartDataModel, List[SmartDataModel], List[Util], None]
Relationship = Union[str, List[str]]
GeoProperty = Union[Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, Feature, FeatureCollection]


def to_ngsi_ld(obj: SmartDataModel):
    if not isinstance(obj, SmartDataModel):
        raise TypeError(f"Expected SmartDataModel, got {type(obj)}")

    entity = Entity(obj.type, obj.id)
    entity.ctx.append(obj.ctx)
    for field in dataclasses.fields(obj):
        field_value = getattr(obj, field.name)
        if field_value is None or field.name == "id" or field.name == "type":
            continue

        if field.type == Property:
            entity.prop(field.name, field_value)
        elif field.type == Relationship or field.type == Optional[Relationship]:
            entity.rel(field.name, field_value)
        elif field.type == GeoProperty:
            # NOTE: The underlying library only accepts
            # [Point, LineString, Polygon, MultiPoint]
            # as valid geojson inputs at this point. The current
            # workaround is to store location as a regular prop.

            # entity.gprop(field.name, field_value)
            entity.prop(field.name, field_value)

    return entity


def to_object(entity: Entity):
    if not isinstance(entity, Entity):
        raise TypeError(f"Expected {Entity}, got {type(entity)}")

    import sd_data_adapter.models as sd
    all_model_names = ['agri_food', 'device', 'autonomous_mobile_robot']
    class_name = entity.type.split("/")[-1]
    model_class = None
    for model_name in all_model_names:
        model_package = getattr(sd, model_name)
        if hasattr(model_package, class_name):
            model_class = getattr(model_package, class_name)
            break

    if model_class is None:
        raise Exception("Model not found")

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
