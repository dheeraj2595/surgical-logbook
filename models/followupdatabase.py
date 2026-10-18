from sqlalchemy import String, Integer, Date
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base

class FollowUpDatabase(Base):
    __tablename__ = "Follow up database"
    followupid: Mapped[int] = mapped_column(Integer, autoincrement= True)

    #link to an admission
    admission: Mapped[int] = mapped_column(ForeignKey = "caseadmission.admission_id", nullable=False, index=True)

    followupdate: Mapped[Date] = mapped_column(Date, nullable = False, index = True)


