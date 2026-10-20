from sqlalchemy import select
from sqlalchemy.orm import Session

from models.hospitaldatabase import HospitalDatabase
from schemas.hospital import HospitalCreate, HospitalUpdate

#create
def create_hospital(
    db: Session,
    hospital_data: HospitalCreate
) -> HospitalDatabase:

    new_hospital = HospitalDatabase(
        **hospital_data.model_dump()
    )

    try: 
        db.add(new_hospital)
        db.commit()
        db.refresh(new_hospital)
        return new_hospital
    except Exception:
        db.rollback()
        raise 
        

# READ: Get one hospital by ID
def read_hospital(
    db: Session,
    hospital_id: int
) -> HospitalDatabase | None:

    hospital = db.get(HospitalDatabase, hospital_id)

    return hospital

#Read all hospitals
def readall_hospital(
        db: Session
) -> list[HospitalDatabase]: 
    statement = select(HospitalDatabase).order_by(HospitalDatabase.hospital_name)
    hospitals = db.scalars(statement).all()
    return list(hospitals)


# UPDATE: Update a hospital
def update_hospital(
    db: Session,
    hospital_id: int,
    hospital_name: str,
    hospital_address: str
) -> HospitalDatabase | None:

    hospital = db.get(HospitalDatabase, hospital_id)

    if hospital is None:
        return None

    hospital.hospital_name = hospital_name
    hospital.hospital_address = hospital_address

    try:
        db.commit()
        db.refresh(hospital)
        return hospital
    except Exception:
        db.rollback()
        raise

#Delete a hospital 
def delete_hospital(db: Session, hospital_id: int) -> HospitalDatabase :
    hospital = db.get(HospitalDatabase, hospital_id)
    if hospital is None:
        return False

    try:
        db.delete(hospital)
        db.commit()
        return True
    except Exception:
        db.rollback()
        raise

