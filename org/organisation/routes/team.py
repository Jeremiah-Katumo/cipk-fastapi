from fastapi import FastAPI, status, HTTPException, Path, APIRouter, Form, UploadFile, File
from typing import Annotated, List, Union
from ..schemas import teams_schemas
from ..cruds import team_cruds
from ...database import db_session

 
router = APIRouter(
    prefix="/team",
    tags=['Team']
)

@router.post('/', response_model = teams_schemas.TeamMember)
async def add_new_member(
    db: db_session, 
    name: Annotated[str, Form()], 
    org_id: Annotated[int, Form()], 
    email: Annotated[str, Form()],
    phone: Annotated[str, Form()] = None,
    profile_picture: Annotated[UploadFile, File()] = None,
    position: Annotated[teams_schemas.Positions, Form()] = None,
    social_media_links: Annotated[List[str], Form()] = None
    ):
    member = team_cruds.create_member(
        db = db, 
        name = name, 
        org_id = org_id, 
        profile_picture = profile_picture, 
        position = position, 
        social_media_links = social_media_links,
        phone = phone,
        email = email
        )
    return member

@router.get("/")
def get_all_team_members():
    return {'message': 'List of team member'}

@router.get("/{member_id}")
def get_team_member():
    return {'message':'Team member'}

@router.patch("/")
def update_member():
    return {'message': "Member Updated"}