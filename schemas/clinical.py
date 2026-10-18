from pydantic import BaseModel

class CaseClinical(BaseModel):
    diagnosis: str
    procedure: str
    anaesthesia: str