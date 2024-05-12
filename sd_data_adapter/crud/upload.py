from sd_data_adapter.client import DAClient
from sd_data_adapter.models import to_ngsi_ld, SmartDataModel, to_object


def upload(obj: SmartDataModel):
    if obj is None:
        return None

    with DAClient.get_instance() as client:
        entity = to_ngsi_ld(obj)
        entity.pprint()
        print(f"Saving {entity.id} !")
        return to_object(client.create(entity))