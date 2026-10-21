from pydantic import BaseModel, Field, ConfigDict
from datetime import date

class PatientParticularsCreate(BaseModel):
    name: str = Field(min_length=2, max_length=200)
    date_of_birth: date = Field
    sex: str = Field(min_length=1, max_length=6)
    phone_number: str = Field(min_length=10, max_length=14)
    address: str = Field(min_length=4, max_length=200)
    religion: str | None = Field(min_length = 2, max_length=100)

class PatientParticularsUpdate(BaseModel):
    name: str | None = Field(min_length=2, max_length=200)
    date_of_birth: date | None = Field
    sex: str | None = Field(min_length=1, max_length=6)
    phone_number: str | None = Field(min_length=10, max_length=14)
    address: str | None = Field(min_length=4, max_length=200)
    religion: str | None = Field(min_length = 2, max_length=100)    

class PatientParticularsRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    patient_id : int
    name: str
    date_of_birth: date
    sex: str
    phone_number: str
    address: str
    religion: str