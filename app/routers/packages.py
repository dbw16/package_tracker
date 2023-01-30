import datetime

from fastapi import APIRouter, Depends, HTTPException, status
import app.schemas as schemas
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app import models

router = APIRouter()


@router.get("/package/{package_id}", tags=["packages"], response_model=schemas.PackageDB)
async def get_package_by_id(package_id: int, db: Session = Depends(get_db)) -> models.Package:
    package = crud.get_package(
        db=db,
        package_id=package_id,
    )
    if not package:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return package


@router.post("/package", tags=["packages"], response_model=schemas.PackageDB | models.Package)
async def add_package(db: Session = Depends(get_db)) -> schemas.PackageDB | models.Package:

    package = schemas.Package(
        owner_id="dave",
        carrier=schemas.Carrier(name="gls"),
        state=schemas.PackageState.not_shipped,
        expected_delivery_time=datetime.datetime.now(),
    )
    db_package = crud.create_package(db=db, package=package)

    return db_package


@router.delete("/package/{package_id}", tags=["packages"], response_model=schemas.PackageDB)
async def delete_package(package_id: str) -> schemas.PackageDB:
    # TODO valdate input
    # What is the user id? can we use seassions or something
    # remove to db
    package = schemas.Package(
        owner_id="dave",
        carrier=schemas.Carrier(name="gls"),
        state=schemas.PackageState.not_shipped,
        expected_delivery_time=datetime.datetime.now(),
    )

    return package


@router.get("/packages", tags=["packages"], response_model=list[schemas.PackageDB] | list[models.Package])
async def get_packages(
    db: Session = Depends(get_db), user_id: str | None = None
) -> list[schemas.PackageDB] | list[models.Package]:
    if user_id:
        packages = crud.get_packages_by_user_id(db=db, user_id=user_id)
    else:
        packages = crud.get_packages(db=db)
    return packages
