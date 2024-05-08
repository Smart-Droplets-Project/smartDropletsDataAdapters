from ngsildclient import Client
from sd_data_adapter.models import to_object


def get_by_query(params: dict = None):
    with Client() as client:
        try:
            client.query_generator()
            response = client.query_all(**params)
            res_to_obj = []
            for res in response:
                res_to_obj.append(to_object(res))
            return res_to_obj
        except Exception as e:
            print("ERROR: ", str(e))
    return None


if __name__ == '__main__':
    query_params = {
        'type': 'AgriFarm',
        'q': 'description=="Small american farm in Texas"'
    }
    print(get_by_query(query_params))
