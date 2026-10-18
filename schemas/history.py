from pydantic import BaseModel

class CaseHistory(BaseModel):
    chief_complaint: str
    past_medical_history: str
    past_surgical_history: str
    family_history: str
    social_history: str

class CasePreviousMedications():
    medications: str
    allergies: str