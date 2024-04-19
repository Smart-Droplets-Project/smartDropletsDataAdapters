from enum import Enum


class CropStatus(Enum):
    SEEDED = "seeded"
    JUST_BORN = "justBorn"
    GROWING = "growing"
    MATURING = "maturing"
    READY_FOR_HARVESTING = "readyForHarvesting"
