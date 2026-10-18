from pydantic import BaseModel
from datetime import date
from investigations import CaseInvestigations
from examination import CaseExamination, CaseVitals

class followup(BaseModel):
    followup_date: date
    followup_complaints: str
    followup_vitals: CaseVitals
    followup_examination: CaseExamination
    followup_investigation: CaseInvestigations
    followup_notes: str
