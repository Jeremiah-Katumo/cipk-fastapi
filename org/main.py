from fastapi import FastAPI
from . import schemas, crud
from .routes import org, contact_us

app = FastAPI()

@app.get("/", tags=['Home'])
async def root():
    return {'message': 'Welcome to CIPK API'} 

app.include_router(org.router)
app.include_router(contact_us.router)


