from abc import ABC, abstractmethod


class carrier_base(ABC):
    @abstractmethod
    def test(self) -> dict[str, int]:
        ...
