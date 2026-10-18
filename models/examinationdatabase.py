
from datetime import datetime


from sqlalchemy import DateTime, ForeignKey, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class AdmissionAssessmentDB(Base):
    __tablename__ = "admission_assessments"

    id: Mapped[str] = mapped_column(
        String(20),
        primary_key=True,
        index = True
        
    )

    admission_id: Mapped[str] = mapped_column(
        ForeignKey("caseadmission.admission_id"),
        nullable=False,
        
    )

    examination_datetime: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now,
    )

    # Vitals
    blood_pressure: Mapped[str | None] = mapped_column(
        String(20), nullable=True
    )
    pulse_rate: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    respiratory_rate: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    spo2: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    temperature: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
    rbs: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )

    # Examination findings
    general_examination: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )
    systemic_examination: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )
    local_examination: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )
