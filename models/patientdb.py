from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class PatientDB(Base):
    __tablename__ = "patients"

    patient_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    date_of_birth: Mapped[Date] = mapped_column(
        Date,
        nullable=True
    )

    sex: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    phone_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    address: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    religion: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )