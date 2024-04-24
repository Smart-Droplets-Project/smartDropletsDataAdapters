from dataclasses import dataclass
from typing import Optional, List

from sd_data_adapter.models.agrifood.AgriParcel import AgriParcel
from sd_data_adapter.models.agrifood.AgriProductType import AgriProductType
from sd_data_adapter.models.util.Operation.OperationType import OperationType
from sd_data_adapter.models.util.Operation.OperationResult import OperationResult
from sd_data_adapter.models.util.Operation.WaterSource import WaterSource


@dataclass
class AgriParcelOperation:
    """

    This class represents an agricultural parcel operation.

    Attributes:
    - id (str): The unique identifier of the operation.
    - type (str): The type of the operation.
    - hasAgriParcel (List[AgriParcel | str]): The agricultural parcel(s) associated with the operation.
    - plannedStartAt (str): The planned start date and time of the operation.
    - plannedEndAt (str): The planned end date and time of the operation.

    Optional Attributes:
    - alternateName (Optional[str]): An alternate name for the operation. (default: None)
    - dataProvider (Optional[str]): The data provider of the operation. (default: None)
    - dataCreated (Optional[str]): The date of creation of the operation data. (default: None)
    - dateModified (Optional[str]): The date of last modification of the operation data. (default: None)
    - description (Optional[str]): The description of the operation. (default: None)
    - startedAt (Optional[str]): The actual start date and time of the operation. (default: None)
    - endedAt (Optional[str]): The actual end date and time of the operation. (default: None)
    - hasAgriProductType (Optional[List[AgriProductType | str]]): The agricultural product type(s) associated with the operation. (default: None)
    - hasOperator (Optional[str]): The operator of the operation. (default: None)
    - irrigationRecord (Optional[str]): The relationship with the irrigation record of the execution. (default: None)
    - operationType (Optional[OperationType]): The type of operation. (default: None)
    - owner (Optional[List[str]]): The owner(s) of the operation. (default: None)
    - quantity (Optional[float]): The quantity of the operation. (default: None)
    - relatedSource (Optional[List[str]]): The related source(s) of the operation. (default: None)
    - reportedAt (Optional[str]): The date and time when the operation was reported. (default: None)
    - result (Optional[OperationResult]): The result of the operation. (default: None)
    - status (Optional[str]): The status of the operation. (default: None)
    - waterSource (Optional[WaterSource]): The water source of the operation. (default: None)
    - workOrder (Optional[str]): The work order of the operation. (default: None)
    - workRecord (Optional[str]): The work record of the operation. (default: None)
    - seeAlso (Optional[List[str]]): Other resources related to the operation. (default: None)
    - source (Optional[List[str]]): The source(s) of the operation. (default: None)

    """
    id: str
    type: str
    hasAgriParcel: List[AgriParcel | str]
    plannedStartAt: str
    plannedEndAt: str


    alternateName: Optional[str] = None
    dataProvider: Optional[str] = None
    dataCreated: Optional[str] = None
    dateModified: Optional[str] = None
    description: Optional[str] = None
    startedAt: Optional[str] = None
    endedAt: Optional[str] = None
    hasAgriProductType: Optional[List[AgriProductType | str]] = None
    hasOperator: Optional[str] = None
    irrigationRecord: Optional[str] = None
    operationType: Optional[OperationType] = None
    owner: Optional[List[str]] = None
    quantity: Optional[float] = None
    relatedSource: Optional[List[str]] = None
    reportedAt: Optional[str] = None
    result: Optional[OperationResult] = None
    status: Optional[str] = None
    waterSource: Optional[WaterSource] = None
    workOrder: Optional[str] = None
    workRecord: Optional[str] = None
    seeAlso: Optional[List[str]] = None
    source: Optional[List[str]] = None

