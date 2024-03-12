from fastapi import FastAPI
from .organisation.models import org_models
from .organisation.routes import entity, contact_us, team, gallery, faqs
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

org_models.Base.metadata.create_all(bind=engine)

@app.get("/", tags=['Home'])
async def root():
    return {'message': 'Welcome to CIPK API'} 

app.include_router(entity.router)
app.include_router(contact_us.router)
app.include_router(team.router)
app.include_router(gallery.router)
app.include_router(faqs.router)

