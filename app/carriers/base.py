from abc import ABC, abstractmethod
from app import schemas


class carrier_base(ABC):
    @abstractmethod
    def test(self) -> dict[str, int]:
        ...

    @property
    @abstractmethod
    def id(self) -> str:
        ...

    @abstractmethod
    def look_up_package(self) -> schemas.PackageDB:
        ...
