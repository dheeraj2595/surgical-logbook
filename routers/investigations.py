from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db
from CRUD import investigation as investigation_crud
from schemas.investigations import (
    CaseInvestigationsCreate,
    CaseInvestigationsUpdate,
)

router = APIRouter(
    prefix="/investigations",
    tags=["Investigations"],
)


# CREATE an investigation
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_investigation(
    investigation: CaseInvestigationsCreate,
    db: Session = Depends(get_db),
):
    return investigation_crud.investigationcreate(db, investigation)


# READ one investigation
@router.get("/{investigation_id}")
def read_investigation(
    investigation_id: int,
    db: Session = Depends(get_db),
):
    investigation = investigation_crud.readinvestigation(
        db, investigation_id
    )

    if investigation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Investigation not found",
        )

    return investigation


# READ all investigations
@router.get("/")
def read_all_investigations(
    db: Session = Depends(get_db),
):
    return investigation_crud.readinvestigationall(db)


# UPDATE an investigation
@router.put("/{investigation_id}")
def update_investigation(
    investigation_id: int,
    investigation_data: CaseInvestigationsUpdate,
    db: Session = Depends(get_db),
):
    investigation = investigation_crud.investigationupdate(
        db,
        investigation_data,
        investigation_id,
    )

    if investigation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Investigation not found",
        )

    return investigation


# DELETE an investigation
@router.delete("/{investigation_id}")
def delete_investigation(
    investigation_id: int,
    db: Session = Depends(get_db),
):
    deleted = investigation_crud.investigationdelete(
        db, investigation_id
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Investigation not found",
        )

    return {"message": "Investigation deleted successfully"}