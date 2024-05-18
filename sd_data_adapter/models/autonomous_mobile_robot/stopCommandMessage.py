from dataclasses import dataclass
from typing import Optional

from .. import AutonomousMobileRobot, Property


@dataclass
class StopCommandMassage(AutonomousMobileRobot):
    """
    Class representing a stop command message for an autonomous mobile robot.

    This class inherits from the `AutonomousMobileRobot` class.

    Attributes:
        commandTime (Optional[Property]): The time that the stop command was sent. Defaults to `None`.
        stopCommand (Optional[Property]): The stop command to be executed. Defaults to `None`.
    """
    
    commandTime: Optional[Property] = None
    stopCommand: Optional[Property] = None