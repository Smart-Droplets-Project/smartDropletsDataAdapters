from typing import Union

from ngsildclient.api.batch import BatchResult

from ..client import DAClient
from ..models import to_ngsi_ld, SmartDataModel, to_object


def update(obj: SmartDataModel) -> Union[bool, BatchResult]:
    if not isinstance(obj, SmartDataModel):
        raise TypeError(f'Expected a SmartDataModel, got {type(obj)}')

    if obj is None:
        raise ValueError('Object cannot be None')

    with DAClient.get_instance() as client:
        entity = to_ngsi_ld(obj)
        print(f"Updating {entity.id} !")
        return client.update(entity)


def upsert(obj: SmartDataModel) -> Union[bool, BatchResult]:
    '''
    Upsert a single instance of a SmartDataModel
    '''
    if not isinstance(obj, SmartDataModel):
        raise TypeError(f'Expected a SmartDataModel, got {type(obj)}')

    if obj is None:
        raise ValueError('Object cannot be None')

    with DAClient.get_instance() as client:
        entity = to_ngsi_ld(obj)
        print(f"Upserting {entity.id} !")
        return client.upsert(entity)
    