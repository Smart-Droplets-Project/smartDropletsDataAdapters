from ngsildclient import Client

from sd_data_adapter.models.agrifood import AgriParcel, AgriPest, AgriFarm
from sd_data_adapter.models import to_ngsi_ld, SmartDataModel


def upload(obj: SmartDataModel):
    if obj is None:
        return None

    with Client() as client:
        entity = to_ngsi_ld(obj)
        entity.pprint()
        print(f"Saving {entity.id} !")
        return client.create(entity)


if __name__ == "__main__":
    agriCrop = AgriFarm(hasAgriParcel=["urn:ngsi-ld:AgriParcel:e27dbb51-05d0-4457-b461-b0d89692c69e-id"], description="Small")
    upload(agriCrop)