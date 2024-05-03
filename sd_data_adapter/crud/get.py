from ngsildclient import Client
from sd_data_adapter.models import to_object


def get(id: str):
    if id is None or len(id) == 0:
        return None

    with Client() as client:
        entity = client.get(id)

    return to_object(entity)

print(get("urn:ngsi-ld:AgriFarm:4d6857e5-e025-4654-ad59-f665aa8076b9-id"))