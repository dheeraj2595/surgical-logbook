
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.connection import get_db
from CRUD import patient as patient_crud
from schemas.patient import (
    PatientParticularsCreate,
    PatientParticularsRead,
    PatientParticularsUpdate,
)

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


# CREATE: Add a patient
@router.post(
    "/",
    response_model=PatientParticularsRead,
    status_code=status.HTTP_201_CREATED
)
def create_patient(
    patient: PatientParticularsCreate,
    db: Session = Depends(get_db)
):
    return patient_crud.createpatient(db, patient)


# READ: Get one patient by ID
@router.get(
    "/{patient_id}",
    response_model=PatientParticularsRead
)
def read_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = patient_crud.readpatient(db, patient_id)

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    return patient


# UPDATE: Update a patient
@router.put(
    "/{patient_id}",
    response_model=PatientParticularsRead
)
def update_patient(
    patient_id: int,
    patient_data: PatientParticularsUpdate,
    db: Session = Depends(get_db)
):
    patient = patient_crud.updatepatient(
        db, patient_data, patient_id
    )

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    return patient


# DELETE: Delete a patient
@router.delete("/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    deleted = patient_crud.deletepatient(db, patient_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found"
        )

    return {"message": "Patient deleted successfully"}
