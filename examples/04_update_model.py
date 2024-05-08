from datetime import datetime

from sd_data_adapter.crud import get_by_id, update

# Here is an example of updating
# I will use method get_by_id to get an instance from database and will update
# dateModified property and then use upload method sd_data_adapter.crud

if __name__ == '__main__':
    model = get_by_id("urn:ngsi-ld:AgriFarm:1cece927-99c7-4fdc-a555-eb4b1f2cdea9-id")
    setattr(model, "dateModified", str(datetime.now()))
    model = update(model)
    print(model)