from sd_data_adapter.client import DAClient
from sd_data_adapter.models import to_object


def get_by_id(id: str):
    if id is None or len(id) == 0:
        return None

    with DAClient.get_instance() as client:
        entity = client.get(id)
        entity.pprint()

    return to_object(entity)


def search(params: dict = None):
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
