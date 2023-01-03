from fastapi import APIRouter
import typing as t
from app.carriers import base
from app.carriers import gls
from app.carriers import fedex
import app.schemas as schemas
import asyncio

router = APIRouter()


@router.get("/carriers/", tags=["carriers"], response_model=list[schemas.Carrier])
async def read_carriers() -> list[schemas.Carrier]:
    return [schemas.Carrier(name=name.__name__) for name in base.carrier_base.__subclasses__()]


# asyncio.run(read_carriers())
