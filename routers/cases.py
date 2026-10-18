
from datetime import date
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.connection import get_db



router = APIRouter(
    prefix="/cases",
    tags=["Surgical Cases"],
)


class CaseCreate(BaseModel):
    diagnosis: str = Field(min_length=1, max_length=150)
    procedure: str = Field(min_length=1, max_length=150)
    surgery_date: date


class SurgicalCase(CaseCreate):
    id: str


