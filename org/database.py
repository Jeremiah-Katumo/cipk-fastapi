from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends

pymysql.install_as_MySQLdb()
# SQLALCHEMY_DATABASE_URL = "sqlite:///./cipk-dev.db"

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Compassion123@localhost:5433/cipk"

SQLALCHEMY_DATABASE_URL = 'mysql+mysqldb://toolkit:Compassion123@localhost:3306/cipk_fastapi'

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_session = Annotated[Session, Depends(get_db)]