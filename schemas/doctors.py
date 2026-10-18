from pydantic import BaseModel

class Doctors(BaseModel):
    name: str
    age: int | None = None
    sex: str
    HomeState: str | None = None
    HomeDistrict: str | None = None
    HomeTown: str | None = None
    designation: str | None = None
    department: str | None = None
    registration_number: str | None = None
    MBBSbatch: str | None = None
    MBBScollege: str | None = None
    PGbatch: str | None = None
    PGcollege: str | None = None
    SSbatch: str | None = None
    SScollege: str | None = None

class CaseDoctors(BaseModel):
    primary_doctor: Doctors
    secondary_doctor: Doctors | None = None

class nurse(BaseModel): 
    name: str
    age: int | None = None
    sex: str
    designations: str | None = None

class CaseSurgery(BaseModel):
    chief_surgeon: Doctors
    chief_anaesthetist: Doctors
    assistant_anaesthetist: Doctors | None = None
    firstassistant: Doctors
    secondassistant: Doctors | None = None
    thirdassistant: Doctors | None = None
    fourthassistant: Doctors | None = None 
    fifthassistant: Doctors | None = None
    scrubnurse: nurse | None = None
    floornurse: nurse | None = None