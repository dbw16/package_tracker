from __future__ import annotations

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Table, MetaData
from sqlalchemy.orm import relationship, Mapped
from sqlalchemy.orm import mapped_column
from app.database import Base, metadata
from app.schemas import PackageState


class Package(Base):
    __tablename__ = "packages"
    id: Mapped[int] = mapped_column(Integer, init=False, primary_key=True, autoincrement=True)
    owner_id: Mapped[str] = mapped_column(String, unique=False, index=True)
    carrier: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(Enum(PackageState))
