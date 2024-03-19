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
    name: str 
    image: UploadFile
    position: Positions
    social_media_links: Union[List[str], None] = None
    
class Team(BaseModel):
    team_members: Union[List[TeamMember], None] = None