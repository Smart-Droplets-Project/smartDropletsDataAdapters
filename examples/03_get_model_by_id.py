from sd_data_adapter.crud import get_by_id

# Here is an example of getting a model from database based on id value
# To be able to get it by id, we have to import the method get_by_id from sd_data_adapter.crud
# It returns an instance of SmartDataModel subclass

if __name__ == '__main__':
    model = get_by_id("urn:ngsi-ld:AgriFarm:1cece927-99c7-4fdc-a555-eb4b1f2cdea9-id")
    print(model)