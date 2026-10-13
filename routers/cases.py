from datetime import date
from uuid import uuid4

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/cases",
    tags=["surgical cases"])

#temporary storage for cases

cases = []

class CaseCreate(BaseModel):
    diagnosis: str = Field(min_length=1, max_length=150)
    procedure: str = Field(min_length=1, max_length=150)
    surgery_date: date

class SurgicalCase(CaseCreate):
    id: str

@router.get("/", response_model=list[SurgicalCase])
def get_cases():
    return cases

@router.post("/", response_model=SurgicalCase, status_code=201)
def create_case(case: CaseCreate):
    new_case = SurgicalCase(
        id=f"PS-{uuid4().hex[:12].upper()}",
        **case.model_dump(),
    )

    cases.append(new_case)
    return new_case


@router.get("/{case_id}", response_model=SurgicalCase)
def get_case(case_id: str):
    for case in cases:
        if case.id == case_id:
            return case

    raise HTTPException(status_code=404, detail="Case not found")