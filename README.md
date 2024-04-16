# Smart Droplets Data Adapter

## Overview

The Smart Droplets Data Adapter Library is a Python package designed to facilitate the encoding and decoding of agricultural, IoT, and robotics entities to and from NGSI-LD format. It is intended to be used within the context of the [Smart Droplets Horizon 2020 project](https://smartdroplets.eu/), providing seamless integration with the NGSI-LD standard and [Smart Data Models](https://smartdatamodels.org/), through a set of utility functions designed around Smart Droplets concepts. These utility functions can be used by all components of the Smart Droplets ecosystem to easily exchange context information.

## Features

Encode and decode agricultural, IoT, and robotics entities to and from NGSI-LD format.
Supports entities from the Smart Data Models Agrifood & Device vocabularies.
Provides functions for handling entities such as Farms, Parcels, Crops, CommandMessages, etc.

## Installation

To install the Smart Droplets Data Adapter Library, you can use pip:

```bash
pip install sd_data_adapter
```

## Dependencies

- ngsildclient
    - [ngsildclient](https://pypi.org/project/ngsildclient/) is a Python client library for NGSI-LD APIs.

## Usage

TODO: Insert real code snippet

```py
from horizon_ngsi_ld import encode_entity, decode_entity

# Example entity
entity = {
    "id": "urn:ngsi-ld:Farm:001",
    "type": "Farm",
    "name": {
        "value": "Example Farm"
    },
    "location": {
        "type": "Point",
        "coordinates": [40.7128, -74.0060]
    }
}

# Encode entity to NGSI-LD format
ngsi_ld_entity = encode_entity(entity)

# Decode NGSI-LD entity
decoded_entity = decode_entity(ngsi_ld_entity)
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

TODO: Check