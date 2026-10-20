from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db
from CRUD import hospital as hospital_crud
from schemas.hospital import (
    HospitalCreate,
    HospitalUpdate,
    HospitalRead,
)

router = APIRouter(
    prefix="/hospitals",
    tags=["Hospitals"]
)


# CREATE
@router.post(
    "/",
    response_model=HospitalRead,
    status_code=status.HTTP_201_CREATED
)
def create_hospital(
    hospital_data: HospitalCreate,
    db: Session = Depends(get_db)
):
    return hospital_crud.create_hospital(db, hospital_data)


# READ: one hospital
@router.get("/{hospital_id}", response_model=HospitalRead)
def read_hospital(
    hospital_id: int,
    db: Session = Depends(get_db)
):
    hospital = hospital_crud.read_hospital(db, hospital_id)

    if hospital is None:
        raise HTTPException(
            status_code=404,
            detail="Hospital not found"
        )

    return hospital


# READ: all hospitals
@router.get("/", response_model=list[HospitalRead])
def read_all_hospitals(
    db: Session = Depends(get_db)
):
    return hospital_crud.read_all_hospitals(db)


# UPDATE
@router.put("/{hospital_id}", response_model=HospitalRead)
def update_hospital(
    hospital_id: int,
    hospital_data: HospitalUpdate,
    db: Session = Depends(get_db)
):
    hospital = hospital_crud.update_hospital(
        db, hospital_id, hospital_data
    )

    if hospital is None:
        raise HTTPException(
            status_code=404,
            detail="Hospital not found"
        )

    return hospital


# DELETE
@router.delete("/{hospital_id}")
def delete_hospital(
    hospital_id: int,
    db: Session = Depends(get_db)
):
    deleted = hospital_crud.delete_hospital(db, hospital_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Hospital not found"
        )

    return {"message": "Hospital deleted successfully"}
