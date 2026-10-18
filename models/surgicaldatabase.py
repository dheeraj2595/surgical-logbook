
from datetime import date
from sqlalchemy import Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class CaseSurgeryDB(Base):
    __tablename__ = "case_surgery"

    surgery_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    admission_id: Mapped[int] = mapped_column(
        ForeignKey("caseadmission.admission_id"),
        nullable=False,
        index=True,
    )

    surgery_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    anaesthesia_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    surgery_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    surgery_duration: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    surgery_findings: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    surgery_complications: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    surgery_orders: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    surgery_note: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
