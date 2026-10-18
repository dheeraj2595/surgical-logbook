from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class HospitalDB(Base):
    __tablename__ = "hospitals"

    hospital_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    hospital_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    hospital_address: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )