from fastapi import FastAPI, status, HTTPException

from .crud import create_org, get_org
from . import schemas

app = FastAPI()



@app.get("/")
async def root():
    return {'message': 'Welcome to CIPK API'} 


@app.get("/org/{org_id}", response_model=schemas.OrgOut)
def get_org(org_id: int):
    org = get_org(org_id)
    return org 


@app.post("/org/", status_code=status.HTTP_201_CREATED, response_model=schemas.OrgOut)
def create_org(org: schemas.OrgIn):
    org = create_org(org)
    return org

@app.patch("/org/{org_id}")
def update_org(org_id: int, org: schemas.OrgIn):
    org = update_org(org)
    return {'message': 'Org has been updated'}


@app.post("/contact_us")
def contact_us():
    return {'message': 'Message sent'}
