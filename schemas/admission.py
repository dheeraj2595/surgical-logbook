
from pydantic import BaseModel
import datetime

class hospitaldatabase(BaseModel):
    hospital_ID: str
    hospital_name: str
    hospital_address: str
    
class CaseAdmission(BaseModel):
    hospital_ward: str
    hospital_bed_number: str
    hospital_admission_date: datetime
    hospital_discharge_date: datetime
    age_at_admission: int
