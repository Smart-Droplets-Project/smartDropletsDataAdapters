from enum import Enum

from sd_data_adapter.models import Util


class ProductCategory(Util, Enum):
    """

    Enum for different product categories.

    Attributes:
        FERTILISER (str): Category for fertilisers.
        CROP_NUTRITION (str): Category for crop nutrition products.
        CROP_PROTECTION (str): Category for crop protection products.
        CROP_VARIETY (str): Category for crop variety.
        HARVEST_COMMODITY (str): Category for harvested commodities.

    """

    FERTILISER = "fertiliser"
    CROP_NUTRITION = "cropNutrition"
    CROP_PROTECTION = "cropProtection"
    CROP_VARIETY = "cropVariety"
    HARVEST_COMMODITY = "harvestCommodity"