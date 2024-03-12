from fastapi import FastAPI, status, HTTPException, Path, APIRouter
from typing import Annotated
from ..schemas import schemas
from ..cruds import cruds


router = APIRouter(
    prefix="/org",
    tags=['Oragnization']
)

@router.get("/{org_id}", response_model=schemas.OrgOut)
def get_org(org_id: Annotated[int, Path(gt = 0)]):
    """
    ## Introduction:

    This endpoint gets all information to be use in the welcome page of the CIPK website
    """
    org = cruds.get_org(org_id)
    return org 


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.OrgOut)
def create_org(org: schemas.OrgIn):
    org = cruds.create_org(org)
    return org

@router.patch("/{org_id}")
def update_org(org_id: int, org: schemas.OrgIn):
    org = cruds.update_org(org_id, org)
    return org
