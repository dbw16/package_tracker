import datetime

from fastapi import APIRouter
import typing as t
from app.carriers import base
from app.carriers import gls
from app.carriers import fedex
import app.schemas as schemas
import asyncio

router = APIRouter()


@router.get("/packages/", tags=["packages"], response_model=list[schemas.DataPackage])
async def get_packages() -> list[schemas.DataPackage]:
    packages = [
        schemas.DataPackage(
            owner_id="dave",
            carrier=schemas.Carrier(name="gls"),
            state=schemas.PackageState.not_shipped,
            expected_delivery_time=datetime.datetime.now(),
        )
    ]
    return packages


# asyncio.run(read_carriers())
