from datetime import date, datetime

from sqlalchemy import Date, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base

class SurgicalCaseDb(Base):
    __tablename__ = "Plastic Surgery Cases"

    id : Mapped[str] = mapped_column(String(20), primary_key=True)
    diagnosis: Mapped[str] = mapped_column(String(150),nullable=False)
    procedure: Mapped[str] = mapped_column(String(150),nullable=False)
    surgery_date: Mapped[date] = mapped_column(Date, nullable = False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
