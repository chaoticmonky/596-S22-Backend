from lib2to3.pgen2.token import SLASH
from venv import create
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATEBASE_URL = ""

engine = create_engine(
    SQLALCHEMY_DATEBASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()