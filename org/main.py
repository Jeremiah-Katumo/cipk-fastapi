from fastapi import FastAPI
from . import schemas, crud, models
from .routes import org, contact_us
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/", tags=['Home'])
async def root():
    return {'message': 'Welcome to CIPK API'} 

app.include_router(org.router)
app.include_router(contact_us.router)


