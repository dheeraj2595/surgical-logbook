from pydantic import BaseModel
from datetime import date, time

class CaseSurgery(BaseModel):
    surgery_name: str
    anaesthesia_name: str
    surgery_date: date
    surgery_duration: str
    surgery_findings: str
    surgery_complications: str | None = None
    surgery_orders: str | None = None
    surgery_note: str | None = None
