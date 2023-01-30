import datetime

from .base import carrier_base
from dataclasses import dataclass
import typing as t
from app import schemas


@dataclass
class fedex(carrier_base):
    id: t.ClassVar[str] = "fedex"

    def test(self) -> dict[str, int]:
        return {"nice": 123}

    def look_up_package(self) -> schemas.PackageDB:
        return schemas.PackageDB(
            owner_id="",
            carrier=schemas.Carrier(name=self.id),
            state=schemas.PackageState.in_transit,
            expected_delivery_time=datetime.datetime.now(),
        )
