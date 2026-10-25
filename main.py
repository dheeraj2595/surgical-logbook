from contextlib import asynccontextmanager

from database.connection import Base, engine
from routers.hospitals import router as hospitals_router


from fastapi import FastAPI
from routers.cases import router as cases_router
from routers.patient import router as patients_router
from routers.investigations import router as investigations_router

from models.followupdatabase import FollowUpDatabase
from models.investigationdatabase import InvestigationDB
from models.admissiondatabase import CaseAdmissionDB
from models.hospitaldatabase import HospitalDatabase

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title = "Plastic Surgery logbook", description = "Private plastic surgical logbook", version = "0.1.0", lifespan=lifespan)



@app.get("/")
def home():
    return{"message": "Welcome to the plastic surgery logbook API"}

app.include_router(cases_router)
app.include_router(hospitals_router)
app.include_router(patients_router)
app.include_router(investigations_router)