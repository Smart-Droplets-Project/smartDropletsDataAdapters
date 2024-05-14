from dataclasses import dataclass
from typing import Optional

from sd_data_adapter.models import AutonomousMobileRobot, Property


@dataclass
class StopCommandMassage(AutonomousMobileRobot):
    """
    Class to represent a stop command message for an autonomous mobile robot.

    Attributes:
        accuracy (Optional[Property]): The accuracy of the robot's destination.
        battery (Optional[Property]): The battery level of the robot.
        commandTime (Optional[Property]): The time when the stop command was received.
        destination (Optional[Property]): The destination of the robot.
        errors (Optional[Property]): Any errors that occurred during the execution of the command.
        mode (Optional[Property]): The mode of the robot.
        pose (Optional[Property]): The pose (position and orientation) of the robot.

    """
    
    accuracy: Optional[Property] = None
    battery: Optional[Property] = None
    commandTime: Optional[Property] = None
    destination: Optional[Property] = None
    errors: Optional[Property] = None
    mode: Optional[Property] = None
    pose: Optional[Property] = None