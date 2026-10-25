
from pydantic import BaseModel, Field
from datetime import datetime


class CBC(BaseModel):
    hb: float | None = None
    tlc: float | None = None
    platelets: float | None = None
    hct: float | None = None
    neutrophils: float | None = None
    lymphocytes: float | None = None


class LFT(BaseModel):
    total_bilirubin: float | None = None
    direct_bilirubin: float | None = None
    ast: float | None = None
    alt: float | None = None
    alp: float | None = None
    albumin: float | None = None
    total_protein: float | None = None


class KFT(BaseModel):
    urea: float | None = None
    creatinine: float | None = None
    sodium: float | None = None
    potassium: float | None = None
    chloride: float | None = None


class PTINR(BaseModel):
    pt: float | None = None
    inr: float | None = None


class viral_markers(BaseModel):
    hbsag: str | None = None
    anti_hcv: str | None = None
    hiv: str | None = None


class extras(BaseModel):
    crp: float | None = None
    procalcitonin: float | None = None


class CaseInvestigationsCreate(BaseModel):
    followup_id: int
    investigationtype: str = Field(min_length=1)
    status: str = Field(min_length=1)
    ordered_at: datetime | None = None
    collected_at: datetime | None = None
    reported_at: datetime | None = None
    cbc: CBC | None = None
    lft: LFT | None = None
    kft: KFT | None = None
    pt_inr: PTINR | None = None
    viralmarkers: viral_markers | None = None
    blood_sugar: float | None = None
    extra: extras | None = None


class CaseInvestigationsUpdate(BaseModel):
    investigationtype: str | None = None
    status: str | None = None
    ordered_at: datetime | None = None
    collected_at: datetime | None = None
    reported_at: datetime | None = None
    cbc: CBC | None = None
    lft: LFT | None = None
    kft: KFT | None = None
    pt_inr: PTINR | None = None
    viralmarkers: viral_markers | None = None
    blood_sugar: float | None = None
    extra: extras | None = None
