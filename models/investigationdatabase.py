from datetime import datetime

from sqlalchemy import (
    String,
    Float,
    DateTime,
    Integer,
    ForeignKey,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class InvestigationDB(Base):
    __tablename__ = "investigations"

    investigation_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
    )

    # Link to the relevant postoperative follow-up
    followup_id: Mapped[int] = mapped_column(
        ForeignKey("follow_up_database.followupid"),
        nullable=False,
        index=True,
    )

    # Investigation details
    investigation_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="ordered",
    )

    ordered_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    collected_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    reported_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    # Results for CBC
    hb: Mapped[float | None] = mapped_column(Float, nullable=True)
    tlc: Mapped[float | None] = mapped_column(Float, nullable=True)
    platelets: Mapped[float | None] = mapped_column(Float, nullable=True)
    hct: Mapped[float | None] = mapped_column(Float, nullable=True)
    neutrophils: Mapped[float | None] = mapped_column(Float, nullable=True)
    lymphocytes: Mapped[float | None] = mapped_column(Float, nullable=True)

    # Results for LFT
    total_bilirubin: Mapped[float | None] = mapped_column(Float, nullable=True)
    direct_bilirubin: Mapped[float | None] = mapped_column(Float, nullable=True)
    ast: Mapped[float | None] = mapped_column(Float, nullable=True)
    alt: Mapped[float | None] = mapped_column(Float, nullable=True)
    alp: Mapped[float | None] = mapped_column(Float, nullable=True)
    albumin: Mapped[float | None] = mapped_column(Float, nullable=True)
    total_protein: Mapped[float | None] = mapped_column(Float, nullable=True)

    # Results for KFT
    urea: Mapped[float | None] = mapped_column(Float, nullable=True)
    creatinine: Mapped[float | None] = mapped_column(Float, nullable=True)
    sodium: Mapped[float | None] = mapped_column(Float, nullable=True)
    potassium: Mapped[float | None] = mapped_column(Float, nullable=True)
    chloride: Mapped[float | None] = mapped_column(Float, nullable=True)

    # PT / INR
    pt: Mapped[float | None] = mapped_column(Float, nullable=True)
    inr: Mapped[float | None] = mapped_column(Float, nullable=True)

    # Viral markers
    hbsag: Mapped[str | None] = mapped_column(String(50), nullable=True)
    anti_hcv: Mapped[str | None] = mapped_column(String(50), nullable=True)
    hiv: Mapped[str | None] = mapped_column(String(50), nullable=True)

    # Other investigations
    blood_sugar: Mapped[float | None] = mapped_column(Float, nullable=True)
    crp: Mapped[float | None] = mapped_column(Float, nullable=True)
    procalcitonin: Mapped[float | None] = mapped_column(Float, nullable=True)

    notes: Mapped[str | None] = mapped_column(Text, nullable=True)