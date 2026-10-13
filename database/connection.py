from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#find the root folder of our project
PROJECT_ROOT = Path(__file__).resolve().parent.parent

#create a folder to store the database
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents = True, exist_ok = True)

#Tell sqlalchemy where our sqlite database lives
DATABASE_URL = f"sqlite:///{DATA_DIR/'logbook.db'}"

#create the database engine 
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False},)

#base class for all database models
class Base(DeclarativeBase):
    pass

#factory for creating database sessions
SessionLocal = sessionmaker(expire_on_commit=False, autoflush=False, bind=engine)

#provide a database session to each API request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()