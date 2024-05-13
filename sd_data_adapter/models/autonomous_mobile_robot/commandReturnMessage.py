from dataclasses import dataclass
from typing import Optional

from sd_data_adapter.models import AutonomousMobileRobot, Property


@dataclass
class CommandReturnMessage(AutonomousMobileRobot):
    """

    CommandReturnMessage class represents a message returned by a command execution.

    Attributes:
        commandTime (Optional[Property]): The time at which the command was executed.
        errors (Optional[Property]): Any errors that occurred during the command execution.
        receivedCommand (Optional[Property]): The command that was received.
        receivedTime (Optional[Property]): The time at which the command was received.
        receivedWaypoints (Optional[Property]): The waypoints received as part of the command.
        result (Optional[Property]): The result of the command execution.

    """
    
    commandTime: Optional[Property] = None
    errors: Optional[Property] = None
    receivedCommand: Optional[Property] = None
    receivedTime: Optional[Property] = None
    receivedWaypoints: Optional[Property] = None
    result: Optional[Property] = None