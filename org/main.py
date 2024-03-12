from fastapi import FastAPI
from .organisation.models import models
from .organisation.routes import entity, contact_us
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/", tags=['Home'])
async def root():
    return {'message': 'Welcome to CIPK API'} 

app.include_router(entity.router)
app.include_router(contact_us.router)


