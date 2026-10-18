from pydantic import BaseModel

class CaseParticulars(BaseModel):
    name: str
    age: int
    sex: str
    phone_number: str
    address: str
    religion: str