from sd_data_adapter.client import DAClient
from sd_data_adapter.crud import search

# Here is an example of searching database based on search parameters dictionary
# Params keys: ctx, type, q, limit and max

if __name__ == '__main__':
    DAClient.get_instance()
    search_params = {
        'type': 'AgriFarm',
        'q': 'description=="Small american farm in Texas"'
    }
    models = search(search_params)
    print(models)