from ngsildclient import Client

from sd_data_adapter.models.agrifood.AgriFarm import AgriFarm
from sd_data_adapter.models.agrifood.AgriCrop import AgriCrop


def save(entity: object):
    if entity is None:
        return None

    client = Client()

    ngsi_entity = None
    if isinstance(entity, AgriCrop):
        ngsi_entity = entity.create()
    if isinstance(entity, AgriFarm):
        ngsi_entity = entity.create()

    if ngsi_entity is not None:
        print(f"Saving {ngsi_entity.id}")
        client.create(ngsi_entity)

    client.close()