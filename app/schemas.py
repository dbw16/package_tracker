from datetime import datetime
from dataclasses import dataclass
from pydantic import BaseModel
from enum import Enum, unique


class Carrier(BaseModel):
    name: str


@unique
class PackageState(Enum):
    not_shipped = "Not_Shipped"
    in_transit = "In_Transit"
    out_for_delivery = "Out_For_Delivery"


class Package(BaseModel):
    owner_id: str
    carrier: Carrier
    state: PackageState
    expected_delivery_time: datetime


@dataclass
class DataPackage:
    owner_id: str
    carrier: Carrier
    state: PackageState
    expected_delivery_time: datetime
