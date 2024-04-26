from geojson import Point
from ngsildclient import Client

from sd_data_adapter.models.agrifood import AgriParcel, AgriPest
from sd_data_adapter.models import to_ngsi_ld, SmartDataModel


def upload(obj: SmartDataModel):
    if obj is None:
        return None

    with Client() as client:
        entity = to_ngsi_ld(obj)
        entity.pprint()
        print(f"Saving {entity.id} !")
        client.create(entity)



agriCrop = AgriParcel(None, 2, "urn:ngsi-ld:AgriCrop:7e90b73f-e105-4599-87e2-468675876f3b-id")
upload(agriCrop)