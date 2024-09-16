"""
 Here is an example of searching database based on search parameters dictionary
 Params keys: ctx, type, q, limit and max
"""

from sd_data_adapter.api import search
from sd_data_adapter.models import AgriFood

if __name__ == '__main__':
    search_params = {
        'type': 'AgriFarm',
        'q': 'description=="Small american farm in Texas"'
    }
    models = search(search_params, ctx=AgriFood.ctx)
    print(models[-1])