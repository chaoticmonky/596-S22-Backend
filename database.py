import os
import databases
import sqlalchemy
from schema import notes

DATABASE_URL = "postgresql://postgres:password@localhost:5432/rescue_db_dev"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL
)

# metadata.create_all(engine) ## Populates PostegreSQL table with all data loaded in meta. Not needed since we use alembic