from contextlib import asynccontextmanager

from database.connection import Base, engine
from models.surgical_case import SurgicalCaseDb 

from fastapi import FastAPI
from routers.cases import router as cases_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title = "Plastic Surgery logbook", description = "Private plastic surgical logbook", version = "0.1.0", lifespan=lifespan)



@app.get("/")
def home():
    return{"message": "Welcome to the plastic surgery logbook API"}

app.include_router(cases_router)