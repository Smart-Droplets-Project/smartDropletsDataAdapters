from dataclasses import dataclass
from typing import Optional

from sd_data_adapter.models import AutonomousMobileRobot, Property


@dataclass
class CommandMessage(AutonomousMobileRobot):
    """

    Class CommandMessage

    This class represents a command message for an autonomous mobile robot.

    Attributes:
        command (Optional[Property]): A property representing the command of the robot.
        commandTime (Optional[Property]): A property representing the time of the command.
        waypoints (Optional[Property]): A property representing the waypoints of the robot.

    """

    command: Optional[Property] = None
    commandTime: Optional[Property] = None
    waypoints: Optional[Property] = None