import datetime

import sd_data_adapter.models.agrifood as models

# Here is an example of creating an instance of a model
# ID is generated automatically, but you can pass your desired value
# Type is assigned based on a class you created instance of
# All properties and relationships can be found at https://smartdatamodels.org/dataModel.Agrifood/


if __name__ == '__main__':
    model = models.AgriFarm(
        alternateName="TexFarm",
        description="A farm located in eastern Texas",
        hasBuilding=["House", "Barn"],
        dateCreated=str(datetime.datetime.now()),
        dateModified=str(datetime.datetime.now())
    )

    print(model)
