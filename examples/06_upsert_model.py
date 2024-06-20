"""
 Here is an example of updating
 I will use method get_by_id to get an instance from database and will update
 dateModified property and then use upload method sd_data_adapter.api
"""

import datetime
from sd_data_adapter.api import upsert
from sd_data_adapter.models.agri_food import AgriFarm

if __name__ == '__main__':
    
    farm = AgriFarm(
        alternateName="TexFarm",
        description="A farm in Texas!",
        hasBuilding=["House", "Barn"],
        dateCreated=str(datetime.datetime.now()),
        dateModified=str(datetime.datetime.now())
    )

    print("Inserting model", farm.id)
    upsert(farm)

    farm.description = "An UPDATED farm in Texas!"
    input("Press ANY button to update farm!")

    upsert(farm)