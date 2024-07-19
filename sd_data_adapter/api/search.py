from typing import List, Union

from ..client import DAClient
from ..models import to_object, SmartDataModel


def get_by_id(id: str) -> Union[SmartDataModel, None]:
    if not isinstance(id, str):
        raise TypeError('id must be a string')

    if id is None or len(id) == 0:
        raise ValueError('id cannot be empty')

    with DAClient.get_instance() as client:
        entity = client.get(id)

    if entity is None:
        return None

    return to_object(entity)


def search(params: dict = None) -> Union[List[SmartDataModel], None]:
    allowed_params = ['ctx', 'type', 'q', 'limit', 'max']
    if not isinstance(params, dict):
        raise TypeError('params must be a dict')

    if params is None:
        raise ValueError('params cannot be empty')

    for param in params:
        if param not in allowed_params:
            raise ValueError('Allowed params -> {}'.format(allowed_params))

    with DAClient.get_instance() as client:
        try:
            client.query_generator()
            response = client.query(**params)
            res_to_obj = []
            for res in response:
                res_to_obj.append(to_object(res))
            return res_to_obj
        except Exception as e:
            print("ERROR: ", str(e))
    return None
