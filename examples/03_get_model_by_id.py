"""
 Here is an example of getting a model from database based on id value
 To be able to get it by id, we have to import the method get_by_id from sd_data_adapter.api
 It returns an instance of SmartDataModel subclass
"""

from sd_data_adapter.api import get_by_id
from sd_data_adapter.models import AgriFood

if __name__ == '__main__':
    model = get_by_id("urn:ngsi-ld:AgriFarm:6061c51d-9a9f-428b-900c-759b985868db-id", ctx=AgriFood.ctx)
    print(model)