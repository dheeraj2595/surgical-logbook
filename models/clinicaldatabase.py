from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class CaseClinicalDB(Base):
    __tablename__ = "case_clinical"

    clinical_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    admission_id: Mapped[int] = mapped_column(
        ForeignKey("caseadmission.admission_id"),
        nullable=False,
        index=True,
    )

    diagnosis: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    procedure: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )

    anaesthesia: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
    )
