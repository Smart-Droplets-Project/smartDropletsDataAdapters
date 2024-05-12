from sd_data_adapter.client import DAClient
from sd_data_adapter.crud import get_by_id

# Here is an example of getting a model from database based on id value
# To be able to get it by id, we have to import the method get_by_id from sd_data_adapter.crud
# It returns an instance of SmartDataModel subclass

if __name__ == '__main__':
    DAClient.get_instance()
    model = get_by_id("urn:ngsi-ld:AgriFarm:6061c51d-9a9f-428b-900c-759b985868db-id")
    print(model)