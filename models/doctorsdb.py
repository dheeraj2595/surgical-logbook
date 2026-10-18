from sqlalchemy import Date, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base

now = DateTime.now(DateTime.timezone.utc)
class DoctorDatabase(Base):
    __tablename__ = "Doctors database"

    id: Mapped[int] = mapped_column(primary_key= True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable= False)
    age: Mapped[int] = mapped_column(nullable= True)
    sex: Mapped[str] = mapped_column(String(10), nullable= False)
    homestate: Mapped[str] = mapped_column(String(100), nullable= True)
    homedistrict: Mapped[str] = mapped_column(String(100), nullable= True)
    hometown: Mapped[str] = mapped_column(String(100), nullable= True)
    designation: Mapped[str] = mapped_column(String(100), nullable= True)
    department: Mapped[str] = mapped_column(String(100), nullable= True)    
    registration_number: Mapped[str] = mapped_column(String(150), nullable = True)
    MBBSbatch: Mapped[int] = mapped_column(nullable = True)
    MBBScollege: Mapped[str] = mapped_column(String(100), nullable = True)
    PGbatch: Mapped[int] = mapped_column(nullable = True)
    PGcollege: Mapped[str] = mapped_column(String(150), nullable = True)
    SSbatch: Mapped[str] = mapped_column(String(150), nullable=True)
    SScollege: Mapped[str] = mapped_column(String(150), nullable=True)
    created_at: Mapped[DateTime] = mapped_column(now)

class NurseDatabase(Base):
    __tablename__ = "nurses"
    id: Mapped[int] = mapped_column(primary_key=True, index=True
    )
    name: Mapped[str] = mapped_column(
        String(150), nullable=False
    )
    age: Mapped[int | None] = mapped_column(nullable=True
    )
    sex: Mapped[str] = mapped_column(
        String(20), nullable=False
    )
    designations: Mapped[str | None] = mapped_column(
        String(100), nullable=True
    )