
from fastapi import UploadFile
from datetime import datetime, date
from pydantic import BaseModel, EmailStr
from typing import Union, List
from enum import Enum
from uuid import UUID

class Positions(str, Enum):
    director = "Director"
    pc = "Project Cordinator"

class MessageStatus(str, Enum):
    new = "New"
    replied = "Replied"

class OrgContact(BaseModel):
    email: EmailStr
    phone: str 
    hours: str

class TeamMember(BaseModel):
    name: str 
    image: UploadFile
    position: Positions
    social_media_links: Union[List[str], None] = None

class FAQ(BaseModel):
    question: str 
    answer: str

class GalleryItem(BaseModel):
    heading: str 
    image: UploadFile 
    description: str 

class OrgIn(BaseModel):
    name: str 
    org_uuid: Union[UUID, None] = None
    about: Union[str, None] = None
    location: Union[str, None] = None
    contacts: Union[OrgContact, None] = None
    welcome_message: Union[str, None] = None
    background: Union[str, None] = None
    mission: Union[str, None] = None
    vision: Union[str, None] = None
    core_values: Union[List[str], None] = None
    team_members: Union[List[TeamMember], None] = None
    faqs: Union[List[FAQ], None] = None
    gallery: Union[List[GalleryItem], None] = None


class OrgOut(OrgIn):
    id: int
    created_date: datetime
    updated_date: Union[datetime, None] = None
    created_by: Union[int, None] = None 
    updated_by: Union[int, None] = None 
    org_status: Union[str, None] = 'active'

# class OrgCreateError(BaseModel):
#     message: str

class ContactMessageIn(BaseModel):
    name: str 
    org_id: int
    email: EmailStr 
    subject: str 
    message: str

class ContactMessageOut(ContactMessageIn):
    id: int
    status: Union[str, None] = 'new'
    created_date: date
    updated_date: Union[datetime, None] = None
    created_by: Union[int, None] = None 
    updated_by: Union[int, None] = None 