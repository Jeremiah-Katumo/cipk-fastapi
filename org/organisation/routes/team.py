from fastapi import FastAPI, status, HTTPException, Path, APIRouter, Form, UploadFile, File
from typing import Annotated, List
from ..schemas import teams_schemas
from ..cruds import team_cruds
from ...database import db_session

 
router = APIRouter(
    prefix="/team",
    tags=['Team']
)

@router.post('/')
async def add_new_member(
        db: db_session, 
        name: Annotated[str, Form()], 
        image: Annotated[UploadFile, File()],
        position: Annotated[teams_schemas.Positions, Form()],
        social_media_links: Annotated[List[str], Form()]
    ):
    member = team_cruds.create_member(db, name, image, position, social_media_links)
    return member

@router.get("/")
def get_all_team_members():
    return {'message': 'List of team member'}

@router.get("/{member_id}")
def get_team_member():
    return {'message': 'Team member'}

@router.patch("/")
def update_member():
    return {'message': "Member Updated"}