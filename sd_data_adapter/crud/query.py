from ngsildclient import Client

from sd_data_adapter.crud import get
from sd_data_adapter.models import SmartDataModel, AgriFood, to_object


def get_by_type(type: str, ctx: str =None, params: dict =None):
    with Client() as client:
        try:
            q = client.query_generator(params)
            response = client.query_all(type=type, ctx=ctx)
            for res in response:
                print(str(to_object(res)) + "\n")
        except Exception as e:
            print("ERROR: ", str(e))


if __name__ == '__main__':
    get_by_type("AgriFarm")
