from dataclasses import dataclass
from typing import Optional

from .. import AutonomousMobileRobot, Property


@dataclass
class StopCommandReturnMessage(AutonomousMobileRobot):
    """

    Class: StopCommandReturnMessage

    This class represents a return message for the StopCommand. It inherits from the AutonomousMobileRobot class.

    Attributes:
    - commandTime (Optional[Property]): The time the stop command was initiated.
    - errors (Optional[Property]): Any errors that occurred while executing the stop command.
    - receivedStopCommand (Optional[Property]): Whether the stop command was received.
    - receivedTime (Optional[Property]): The time the stop command was received.
    - resultsOfStopCommand (Optional[Property]): The results of the stop command execution.

    """

    commandTime: Optional[Property] = None
    errors: Optional[Property] = None
    receivedStopCommand: Optional[Property] = None
    receivedTime: Optional[Property] = None
    resultsOfStopCommand: Optional[Property] = None