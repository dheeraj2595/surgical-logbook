
from pydantic import BaseModel, ConfigDict, Field


class HospitalCreate(BaseModel):
    hospital_name: str = Field(min_length=1, max_length=400)
    hospital_address: str = Field(min_length=1, max_length=800)


class HospitalUpdate(BaseModel):
    hospital_name: str | None = Field(
        default=None, min_length=1, max_length=400
    )
    hospital_address: str | None = Field(
        default=None, min_length=1, max_length=800
    )


class HospitalRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    hospital_id: int
    hospital_name: str
    hospital_address: str
