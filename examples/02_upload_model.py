import datetime

import sd_data_adapter.models.agrifood as models
from sd_data_adapter.client import DAClient
from sd_data_adapter.crud import upload

# Here is an example of uploading a model
# I will use parameters from 01_create_model.py
# To be able to save this, we have to import upload method


if __name__ == '__main__':
    DAClient.get_instance()
    model = models.AgriFarm(
        alternateName="TexFarm",
        description="A farm located in eastern Texas",
        hasBuilding=["House", "Barn"],
        dateCreated=str(datetime.datetime.now()),
        dateModified=str(datetime.datetime.now())
    )

    print(upload(model))
