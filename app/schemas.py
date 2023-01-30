from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dataclasses import dataclass
else:
    from pydantic.dataclasses import dataclass
from enum import StrEnum, unique


class ORMConfig:
    orm_mode = True


@dataclass(config=dict(orm_mode=True))  # type: ignore
class Carrier:
    name: str


@unique
class PackageState(StrEnum):
    not_shipped = "Not_Shipped"
    in_transit = "In_Transit"
    out_for_delivery = "Out_For_Delivery"


@dataclass(config=dict(orm_mode=True))  # type: ignore
class PackageBase:
    owner_id: str
    carrier: Carrier
    state: PackageState
    expected_delivery_time: datetime


@dataclass(config=dict(orm_mode=True))  # type: ignore
class PackageDB(PackageBase):
    id: int
