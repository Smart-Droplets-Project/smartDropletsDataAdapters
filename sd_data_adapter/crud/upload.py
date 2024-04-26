from ngsildclient import Client

from sd_data_adapter.models.agrifood import AgriCrop
from sd_data_adapter.models import to_ngsi_ld, SmartDataModel


def upload(obj: SmartDataModel):
    if obj is None:
        return None

    client = Client()
    entity = to_ngsi_ld(obj)
    print(f"Saving {entity.id}!")
    client.create(entity)
    client.close()


agriCrop = AgriCrop('Soyaa')
upload(agriCrop)