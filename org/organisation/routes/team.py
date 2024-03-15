from fastapi import FastAPI, status, HTTPException, Path, APIRouter
from typing import Annotated
# from ..schemas import org_schemas
# from ..cruds import cruds

 
router = APIRouter(
    prefix="/team",
    tags=['Team']
)


@router.get("/")
def get_all_team_members():
    return {'message': 'List of team member'}

@router.get("/{member_id}")
def get_team_member():
    return {'message':'Team member'}

@router.post('/')
def add_new_member():
    return {'message': "Member Added"}

@router.patch("/")
def update_member():
    return {'message': "Member Updated"}