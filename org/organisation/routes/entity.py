from fastapi import FastAPI, status, HTTPException, Path, APIRouter
from typing import Annotated, Union, List
from ..schemas import org_schemas
from ..cruds import org_cruds
from ...database import db_session


router = APIRouter(
    prefix="/org",
    tags=['Organization']
)


@router.get("/", response_model=List[org_schemas.OrgOut])
def get_all_orgs(db: db_session, offset: Union[int, None] = 0, limit: Union[Annotated[int, Path(le=10)], None] = 10):
    orgs = org_cruds.get_all_orgs(db, offset, limit)
    return orgs

@router.get("/{org_id}", response_model=org_schemas.OrgOut)
def get_org(db: db_session, org_id: Annotated[int, Path(gt = 0)]):
    org = org_cruds.get_org(db, org_id)
    return org 


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=org_schemas.OrgOut)
def create_org(db: db_session,org: org_schemas.OrgIn):
    org = org_cruds.create_org(db, org)
    return org

@router.patch("/{org_id}", response_model=org_schemas.OrgOut)
def update_org(db: db_session, org_id: int, org: org_schemas.OrgIn):
    org = org_cruds.update_org(db, org_id, org)
    return org
