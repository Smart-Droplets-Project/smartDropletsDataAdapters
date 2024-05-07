from ngsildclient import Client

from sd_data_adapter.crud import get
from sd_data_adapter.models.agrifood import AgriParcel, AgriPest, AgriFarm
from sd_data_adapter.models import to_ngsi_ld, SmartDataModel


def update(obj: SmartDataModel):
    if obj is None:
        return None

    with Client() as client:
        entity = to_ngsi_ld(obj)
        entity.pprint()
        print(f"Updating {entity.id} !")
        client.update(entity)


if __name__ == "__main__":
    obj = get("urn:ngsi-ld:AgriFarm:4d6857e5-e025-4654-ad59-f665aa8076b9-id")
    print(hasattr(obj, "ownedBy"))
    setattr(obj, "owner", "VizLore Labs")
    update(obj)