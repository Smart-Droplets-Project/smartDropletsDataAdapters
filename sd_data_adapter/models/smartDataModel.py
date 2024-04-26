import dataclasses
from typing import Union, List

from geojson import LineString, Point, Polygon, MultiPoint, MultiLineString, MultiPolygon
from ngsildclient import Entity

from sd_data_adapter.models import Property, Relationship, GeoProperty, Util


@dataclasses.dataclass
class SmartDataModel:
    pass


def to_ngsi_ld(obj: SmartDataModel):
    entity = Entity(obj['type'], f'urn:ngsi-ld:{obj['type']}:{obj['id']}-id')

    for field in dataclasses.fields(obj):
        if obj[field] is None:
            continue

        if isinstance(obj[field], Property):
            entity.prop(field, obj[field])
        elif isinstance(obj[field], Relationship):
            entity.rel(field, obj[field])
        elif isinstance(obj[field], GeoProperty):
            entity.gprop(field, obj[field])

    return entity


def to_object(entity: Entity):
    pass


Property: Union[bool, int, float, str, List[str], SmartDataModel, List[SmartDataModel], List[Util]]
Relationship: Union[str, List[str]]
GeoProperty: Union[Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon]
