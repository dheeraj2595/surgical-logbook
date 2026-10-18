from pydantic import BaseModel

class CaseVitals(BaseModel):
    blood_pressure: int
    pulse_rate: int
    respiratory_rate: int
    sPO2: int
    temperature: int
    rbs: int

class CaseExamination(BaseModel):
    general_examination: str
    systemic_examination: str
    local_examination: str