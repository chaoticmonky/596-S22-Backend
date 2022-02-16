from lib2to3.pgen2.token import SLASH
from venv import create
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATEBASE_URL = "postgresql://postgres:password@localhost:5432/rescue_db_dev"

engine = create_engine(
    SQLALCHEMY_DATEBASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()