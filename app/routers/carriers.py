from fastapi import APIRouter
import typing as t
import app.carriers as carriers
import app.schemas as schemas

router = APIRouter()


@router.get("/carriers/", tags=["carriers"], response_model=list[schemas.Carrier])
async def read_carriers() -> list[schemas.Carrier]:
    return [schemas.Carrier(name=name.__name__) for name in carriers.base.carrier_base.__subclasses__()]


# asyncio.run(read_carriers())
