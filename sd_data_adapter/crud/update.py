from ngsildclient import Client

from sd_data_adapter.models import to_ngsi_ld, SmartDataModel, to_object


def update(obj: SmartDataModel):
    if obj is None:
        return None

    with Client() as client:
        entity = to_ngsi_ld(obj)
        entity.pprint()
        print(f"Updating {entity.id} !")
        return to_object(client.update(entity))