from fastapi import FastAPI, status, HTTPException, Path, APIRouter, Depends
from typing import Annotated
from ..schemas import org_schemas
from ..cruds import org_cruds
from ...database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/org",
    tags=['Organization']
)

db_session = Annotated[Session, Depends(get_db)]

@router.get("/{org_id}", response_model=org_schemas.OrgOut)
def get_org(org_id: Annotated[int, Path(gt = 0)]):
    """
    ## Introduction:

    This endpoint gets all information to be use in the welcome page of the CIPK website
    """
    org = org_cruds.get_org(org_id)
    return org 


@router.post("/", status_code=status.HTTP_201_CREATED) # response_model=org_schemas.OrgOut
def create_org(db: db_session,org: org_schemas.OrgIn):
    org = org_cruds.create_org(db, org)
    return org

@router.patch("/{org_id}")
def update_org(org_id: int, org: org_schemas.OrgIn):
    org = org_cruds.update_org(org_id, org)
    return org
