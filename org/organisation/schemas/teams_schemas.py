from fastapi import UploadFile
from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from typing import Union, List
from enum import Enum
from uuid import UUID


class Positions(str, Enum):
    director = "Director"
    pc = "Project Co-ordinator"
    pm = "Project Manager"
    fm = "Finance Manager"


class TeamMember(BaseModel):
    id: int
    name: str 
    profile_picture: Union[str, None] = None
    position: Union[str, None] = None
    social_media_links: Union[List[str], None] = None
    email: Union[str, None] = None
    phone: Union[str, None] = None
    created_date: datetime
    updated_date: Union[date, None] = None
    created_by: Union[int, None] = None 
    updated_by: Union[int, None] = None 

    class Config:
        orm_mode=True
    
# class Team(BaseModel):
#     team_members: Union[List[TeamMember], None] = None