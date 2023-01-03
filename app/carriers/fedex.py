from .base import carrier_base


class fedex(carrier_base):
    def test(self) -> dict[str, int]:
        return {"nice": 123}
