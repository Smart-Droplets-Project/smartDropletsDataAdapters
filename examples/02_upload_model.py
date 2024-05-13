"""
 Here is an example of uploading a model
 I will use parameters from 01_create_model.py
 To be able to save this, we have to import upload method
"""

import datetime
import sd_data_adapter.models.agrifood as models
from sd_data_adapter.api import upload


if __name__ == '__main__':
    model = models.AgriFarm(
        alternateName="TexFarm",
        description="A farm located in eastern Texas",
        hasBuilding=["House", "Barn"],
        dateCreated=str(datetime.datetime.now()),
        dateModified=str(datetime.datetime.now())
    )

    print(upload(model))
