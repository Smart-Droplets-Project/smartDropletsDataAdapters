import dataclasses
from typing import Union, List

from geojson import LineString, Point, Polygon, MultiPoint, MultiLineString, MultiPolygon
from ngsildclient import Entity


@dataclasses.dataclass
class SmartDataModel:
    pass


class Util:
    pass


Property = Union[bool, int, float, str, List[str], SmartDataModel, List[SmartDataModel], List[Util]]
Relationship = Union[str, List[str]]
GeoProperty = Union[Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon]


def to_ngsi_ld(obj: SmartDataModel):
    entity = Entity(obj.type, f"urn:ngsi-ld:{obj.type}:{obj.id}-id")

    for field in dataclasses.fields(obj):
        field_value = getattr(obj, field.name)
        if field_value is None or field.name == "id" or field.name == "type":
            continue

        if isinstance(field_value, Property):
            entity.prop(field.name, field_value)
        elif isinstance(field_value, Relationship):
            entity.rel(field.name, field_value)
        elif isinstance(field_value, GeoProperty):
            entity.gprop(field.name, field_value)

    return entity


def to_object(entity: Entity):
    pass


