from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base

class HistoryDatabase(Base):
    __tablename__ = "history database"

# CaseHistory fields
    history_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    admission_id: Mapped[int] = mapped_column(ForeignKey("caseadmission.admission_id"), Integer, nullable = False)
    chief_complaint: Mapped[str | None] = mapped_column(String, nullable=True)
    past_medical_history: Mapped[str | None] = mapped_column(String, nullable=True)
    past_surgical_history: Mapped[str | None] = mapped_column(String, nullable=True)
    family_history: Mapped[str | None] = mapped_column(String, nullable=True)
    social_history: Mapped[str | None] = mapped_column(String, nullable=True)

    # CasePreviousMedications fields
    medications: Mapped[str | None] = mapped_column(String, nullable=True)
    allergies: Mapped[str | None] = mapped_column(String, nullable=True)