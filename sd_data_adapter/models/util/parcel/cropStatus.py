from enum import Enum

from sd_data_adapter.models import Util


class CropStatus(Util, Enum):
    """A class representing the status of a crop.

    Attributes:
        SEEDED (str): The crop has been planted as seeds.
        JUST_BORN (str): The crop has just germinated.
        GROWING (str): The crop is growing and developing.
        MATURING (str): The crop is maturing and nearing harvest time.
        READY_FOR_HARVESTING (str): The crop is ready for harvesting.

    """

    SEEDED = "seeded"
    JUST_BORN = "justBorn"
    GROWING = "growing"
    MATURING = "maturing"
    READY_FOR_HARVESTING = "readyForHarvesting"
