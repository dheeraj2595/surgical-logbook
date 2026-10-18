from datetime import datetime

from sqlalchemy import String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class CaseAdmissionDB(Base):
    __tablename__ = "caseadmission"

    admission_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    # Link this admission to a patient
    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.patient_id"),
        nullable=False,
        index=True
    )

    hospital_id: Mapped[int] = mapped_column(ForeignKey("hospitals.hospital_ID"), nullable = False, index = True)

    hospital_ward: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    hospital_bed_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    hospital_admission_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    hospital_discharge_date: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    age_at_admission: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    # CaseHistory fields
    chief_complaint: Mapped[str | None] = mapped_column(String, nullable=True)
    past_medical_history: Mapped[str | None] = mapped_column(String, nullable=True)
    past_surgical_history: Mapped[str | None] = mapped_column(String, nullable=True)
    family_history: Mapped[str | None] = mapped_column(String, nullable=True)
    social_history: Mapped[str | None] = mapped_column(String, nullable=True)

    # CasePreviousMedications fields
    medications: Mapped[str | None] = mapped_column(String, nullable=True)
    allergies: Mapped[str | None] = mapped_column(String, nullable=True)