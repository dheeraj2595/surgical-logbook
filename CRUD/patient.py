from schemas.patient import PatientParticularsCreate, PatientParticularsUpdate
from sqlalchemy.orm import Session
from models.patientdb import PatientDB



def createpatient(db : Session, patient : PatientParticularsCreate) -> PatientDB:
    new_patient = PatientDB(  **patient.model_dump())

    try: 
        db.add(new_patient)
        db.commit()
        db.refresh(new_patient)
        return new_patient
    except Exception: 
        db.rollback()
        raise

def updatepatient(db : Session, patient: PatientParticularsUpdate, patient_id : int) -> PatientDB | None: 
    tobeupdated = db.get(PatientDB, patient_id)
    if tobeupdated is None: 
        return None
    changes = patient.model_dump(exclude_unset=True)

    for field, value in changes.items():
        setattr(tobeupdated, field, value)

    try:
        db.commit()
        db.refresh(tobeupdated)
        return tobeupdated
    except Exception:
        db.rollback()
        raise

def deletepatient(db : Session, patient_id : int) -> bool: 
    tobedeleted = db.get(PatientDB, patient_id)
    if tobedeleted is None: 
        return False

    try: 
        db.delete(tobedeleted)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise

def readpatient(db : Session, patient_id: int) -> PatientDB | None:
    toberead = db.get(PatientDB, patient_id)
    return toberead

