import random

from sqlalchemy.orm import Session
from . import models, schemas
import typing as t


def get_package(db: Session, package_id: int) -> t.Optional[models.Package]:
    return db.query(models.Package).filter(models.Package.id == package_id).first()


def get_packages(db: Session, limit: int = 100) -> list[models.Package]:
    x = db.query(models.Package).limit(limit).all()
    return x


def get_packages_by_user_id(db: Session, user_id: str, limit: int = 100) -> list[models.Package]:
    x = db.query(models.Package).filter(models.Package.owner_id == user_id).all()
    return x


def create_package(db: Session, package: schemas.PackageDB) -> models.Package:
    db_package = models.Package(
        # id=random.randint(0, 1000000000),
        owner_id=package.owner_id,
        carrier=package.carrier.name,
        state=str(package.state.value),
    )
    # x = random.randint(0, 1000000000)
    # db_package.id = x
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package
