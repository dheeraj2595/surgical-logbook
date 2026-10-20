
from pydantic import BaseModel
from datetime import datetime


    
class CaseAdmission(BaseModel):
    admission_id: str
    hospital_ward: str
    hospital_bed_number: str
    hospital_admission_date: datetime
    hospital_discharge_date: datetime | None = None 
    age_at_admission: int
