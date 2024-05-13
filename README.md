# Smart Droplets Data Adapter

## Overview

The Smart Droplets Data Adapter Library is a Python package designed to facilitate the encoding and decoding of agricultural, IoT, and robotics entities to and from NGSI-LD format. It is intended to be used within the context of the [Smart Droplets Horizon project](https://smartdroplets.eu/), providing seamless integration with the NGSI-LD standard and [Smart Data Models](https://smartdatamodels.org/), through a set of utility functions designed around Smart Droplets concepts. These utility functions can be used by all components of the Smart Droplets ecosystem to easily exchange context information.

## Features

Encode and decode agricultural, IoT, and robotics entities to and from NGSI-LD format.
Supports entities from the Smart Data Models Agrifood & Device vocabularies.
Provides functions for handling entities such as Farms, Parcels, Crops, CommandMessages, etc.

## Installation

There are 2 options for including the library into your project:

1. from the project's FTP link (TO BE DEFINED);
1. build & install locally.

### Install from FTP

To install the Smart Droplets Data Adapter Library, you can use pip:

```bash
pip install sd_data_adapter
```

### Install Locally

This option implies cloning the repository, building the library and installing it into your project locally. The steps to do this are:

1. Clone this repository.

1. Navigate to the root directory of the repository/

1. Run the following command to package everything up in a _.tar.gz_:
    
    > python setup.py sdist

1. This will output the following file: _dist/sd_data_adapter-\<version\>.tar.gz_ .

1. Next, navigate to your project and install the library by providing the absolute path to the built library package generated in the previous step.

    > pip install _/path/to/dist/sd_data_adapter-\<version\>.tar.gz_

    Be sure to update the __/path/to__ section of the path to match the absolute path in your local environment.

## Running Examples

The _examples/_ directory contains examples of common use cases such as packaging information into the Smart Droplets data classes, pushing entities to the Orion Context Broker, etc.

In order to run examples, clone the repository and run the following steps.

First, you need an instance of the Orion Context Broker running locally, as the library is a wrapper for communicating with the OCB API. For runningan instance of the Orion Context Broker, please refer to the examples in [this project's repository](https://github.com/Smart-Droplets-Project/contextBrokerExamples) or the [official docker instructions](https://hub.docker.com/r/fiware/orion) provided by FIWARE.

Once this is set up, create a virtual environment where you can install the project dependencies.

> python -m venv venv/

Activate the virtual environment.

> source venv/bin/activate

Install project dependencies into the environment.

> python setup.py install

Run any example, for instane _01_create_model_.

> python -m examples.01_create_model

## Dependencies

- ngsildclient
    - [ngsildclient](https://pypi.org/project/ngsildclient/) is a Python client library for NGSI-LD APIs.

## Usage

```py
import datetime

import sd_data_adapter.models.agrifood as models
from sd_data_adapter.client import DAClient
from sd_data_adapter.crud import upload

# Set up Context Broker client
# In this case, no host/port have been provided,
# which means the client will connect to a local instance 
# of the Orion Context Broker  
DAClient.get_instance()

# Create a Farm using the appropriate data class
model = models.AgriFarm(
    alternateName="TexFarm",
    description="A farm located in eastern Texas",
    hasBuilding=["House", "Barn"],
    dateCreated=str(datetime.datetime.now()),
    dateModified=str(datetime.datetime.now())
)

# Upload model 
upload(model)
```

## Test

In order to run tests, use the unittest Python module like so:

```bash
python -m unittest discover -s test/
```

## License

TODO: Check